import argparse
import inspect
import re
import shlex
import string
from copy import deepcopy
from types import TracebackType
from typing import (
    Dict,
    Generic,
    List,
    NoReturn,
    Optional,
    Tuple,
    Type,
    TypedDict,
    TypeVar,
    Union,
)

from graia.broadcast.entities.dispatcher import BaseDispatcher
from graia.broadcast.entities.signatures import Force
from graia.broadcast.exceptions import ExecutionStop
from graia.broadcast.interfaces.dispatcher import DispatcherInterface

from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Element

from ...event.message import MessageEvent
from ..chain import MessageChain
from .pattern import ArgumentMatch, FullMatch, Match, RegexMatch


class TwilightParser(argparse.ArgumentParser):
    def error(self, message) -> NoReturn:
        raise ValueError(message)

    def accept_type(self, action_str: str) -> bool:
        action_cls: type = self._registry_get("action", action_str, action_str)
        action_init_sig = inspect.signature(action_cls.__init__)
        if "type" not in action_init_sig.parameters:
            return False
        return True


class ArgumentMatchType:
    def __init__(
        self, match: ArgumentMatch, regex: re.Pattern, mapping: Dict[str, Element]
    ):
        self.match = match
        self.regex: re.Pattern = regex
        self.mapping: Dict[str, Element] = mapping

    def __call__(self, string: str) -> MessageChain:
        if self.regex and not self.regex.fullmatch(string):
            raise ValueError(f"{string} not matching {self.regex.pattern}")
        return MessageChain.fromMappingString(string, self.mapping)


class Sparkle:
    def __init__(self, matches: Optional[Dict[str, Match]] = None):
        match_map: Dict[str, Match] = matches or {
            k: v for k, v in self.__class__.__dict__.items() if isinstance(v, Match)
        }
        if any(k.startswith("_") or k[0] in string.digits for k in match_map.keys()):
            raise ValueError("Invalid Match object name!")
        self._regex_match_list: List[Tuple[str, Union[RegexMatch, FullMatch], int]] = []
        group_cnt: int = 0
        pattern_list: List[str] = []
        self._args_map: Dict[str, Tuple[ArgumentMatch, str]] = {}
        for k, v in match_map.items():
            if isinstance(v, Match):
                if isinstance(v, ArgumentMatch):
                    self._args_map[v.name] = (v, k)
                else:
                    self._regex_match_list.append((k, v, group_cnt + 1))
                    group_cnt += re.compile(v.gen_regex()).groups
                    pattern_list.append(v.gen_regex())

        self._regex_pattern = "".join(pattern_list)
        self._regex = re.compile(self._regex_pattern)

    def __repr__(self) -> str:
        repr_dict: Dict[str, Match] = {
            k: v for k, v in self.__dict__.items() if isinstance(v, Match)
        }
        return f"<Sparkle: {repr_dict}>"


T_Sparkle = TypeVar("T_Sparkle", bound=Sparkle)


class TwilightLocalStorage(TypedDict):
    sparkle: Optional[Sparkle]


class Twilight(BaseDispatcher, Generic[T_Sparkle]):
    """
    暮光.
    """

    def __init__(
        self,
        sparkle_cls: Optional[Type[T_Sparkle]] = None,
        remove_quote: bool = True,
        remove_extra_space: bool = False,
        **match_kwargs: Match,
    ):
        """本魔法方法用于初始化本实例.

        Args:
            sparkle (Optional[Type[T_Sparkle]], optional): Sparkle 的子类, 用于生成 Sparkle.
            remove_quote (bool, optional): 处理时是否要移除消息链的 Quote 元素. 默认为 True.
            remove_extra_space (bool, optional): 是否移除 Quote At AtAll 的多余空格. 默认为 False.
            match_kwargs (Match, kwargs): 若未提供 Sparkle 则通过本 kwargs 新建一个.
        Raises:
            ValueError: 同时提供或均未提供 sparkle 与 match_kwargs
        """
        if not bool(sparkle_cls) ^ bool(match_kwargs):  # Both present or both missing
            raise ValueError("Not correct usage!")
        self.sparkle_root: Sparkle = (
            sparkle_cls() if sparkle_cls else Sparkle(match_kwargs)
        )
        self.remove_quote = remove_quote
        self.remove_extra_space = remove_extra_space

    @staticmethod
    def build_arg_parser(
        sparkle: Sparkle, elem_mapping: Dict[str, Element]
    ) -> TwilightParser:
        arg_parser = TwilightParser(exit_on_error=False)
        for match, _ in sparkle._args_map.values():
            add_argument_data = {
                "action": match.action,
                "nargs": match.nargs,
                "default": match.default,
                "required": not match.optional,
            } | (
                {"type": ArgumentMatchType(match, match.regex, elem_mapping)}
                if arg_parser.accept_type(match.action)
                else {}
            )
            arg_parser.add_argument(*match.pattern, **add_argument_data)
        return arg_parser

    @staticmethod
    def dump_namespace(sparkle: Sparkle, namespace: argparse.Namespace) -> None:
        for arg_name, val_tuple in sparkle._args_map.items():
            match, sparkle_name = val_tuple
            namespace_val = getattr(namespace, arg_name, None)
            if arg_name in namespace.__dict__:
                setattr(
                    sparkle,
                    sparkle_name,
                    match.clone(namespace_val, bool(namespace_val)),
                )

    @staticmethod
    def match_regex(
        sparkle: Sparkle, elem_mapping: Dict[str, Element], arg_list: List[str]
    ) -> None:
        if sparkle._regex_pattern:
            if regex_match := sparkle._regex.fullmatch(" ".join(arg_list)):
                for name, match, index in sparkle._regex_match_list:
                    current = regex_match.group(index) or ""
                    setattr(  # sparkle.{name} = to_MessageChain(current)
                        sparkle,
                        name,
                        match.clone(
                            result=MessageChain.fromMappingString(
                                current, elem_mapping
                            ),
                            matched=bool(current),
                            re_match=re.match(match.pattern, current),
                        ),
                    )
            else:
                raise ValueError(f"Regex not matching: {sparkle._regex_pattern}")

    def gen_sparkle(self, chain: MessageChain) -> Sparkle:
        sparkle = deepcopy(self.sparkle_root)
        mapping_str, elem_mapping = chain.asMappingString(
            remove_quote=self.remove_quote, remove_extra_space=self.remove_extra_space
        )
        arg_parser = self.build_arg_parser(sparkle, elem_mapping)
        str_list = shlex.split(mapping_str)
        try:
            namespace, arg_list = arg_parser.parse_known_args(str_list)
            self.dump_namespace(sparkle, namespace)
        except Exception:
            raise
        else:
            self.match_regex(sparkle, elem_mapping, arg_list)
        return sparkle

    def beforeExecution(self, interface: "DispatcherInterface[MessageEvent]"):
        if not isinstance(interface.event, MessageEvent):
            raise ExecutionStop()
        local_storage: TwilightLocalStorage = (
            interface.broadcast.decorator_interface.local_storage
        )
        chain: MessageChain = interface.event.messageChain
        try:
            local_storage["sparkle"] = self.gen_sparkle(chain)
        except:
            raise ExecutionStop()

    async def catch(
        self, interface: "DispatcherInterface[MessageEvent]"
    ) -> Optional[T_Sparkle]:
        local_storage: TwilightLocalStorage = (
            interface.broadcast.decorator_interface.local_storage
        )
        if issubclass(interface.annotation, Sparkle):
            return local_storage["sparkle"]

    def afterExecution(
        self,
        interface: "DispatcherInterface",
        exception: Optional[Exception],
        tb: Optional[TracebackType],
    ):
        del interface.broadcast.decorator_interface.local_storage["sparkle"]
