# (generated with --quick)

from typing import Any, Callable, Dict, Iterable, List, Sized, Tuple, Type, TypeVar, Union

FSimilar = `namedtuple-FSimilar-name-comment-sim_grade`

MsgDef: Any
ProtoDef: Any
Serializer: Any
collections: module
cser_serializer: Any
d_blob: Any
d_string: Any
d_uint32: Any
s_blob: Any
s_string: Any
s_uint32: Any

_Tnamedtuple-FSimilar-name-comment-sim_grade = TypeVar('_Tnamedtuple-FSimilar-name-comment-sim_grade', bound=`namedtuple-FSimilar-name-comment-sim_grade`)

class AddFunction(Any):
    afields: List[str]
    def deserialize(self, msg_data) -> Any: ...
    def serialize(self, msg_inst) -> bytes: ...

class ChooseDB(Any):
    afields: List[str]
    def deserialize(self, msg_data) -> Any: ...
    def serialize(self, msg_inst) -> Any: ...

class FCatalogProtoDef(Any):
    incoming_msgs: Dict[int, Type[Union[AddFunction, ChooseDB, RequestSimilars]]]
    outgoing_msgs: Dict[int, Type[ResponseSimilars]]

class RequestSimilars(Any):
    afields: List[str]
    def deserialize(self, msg_data) -> Any: ...
    def serialize(self, msg_inst) -> bytes: ...

class ResponseSimilars(Any):
    afields: List[str]
    def deserialize(self, msg_data) -> Any: ...
    def serialize(self, msg_inst) -> bytes: ...

class `namedtuple-FSimilar-name-comment-sim_grade`(tuple):
    __slots__ = ["comment", "name", "sim_grade"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str, str]
    comment: Any
    name: Any
    sim_grade: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-FSimilar-name-comment-sim_grade`], name, comment, sim_grade) -> `_Tnamedtuple-FSimilar-name-comment-sim_grade`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-FSimilar-name-comment-sim_grade`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-FSimilar-name-comment-sim_grade`: ...
    def _replace(self: `_Tnamedtuple-FSimilar-name-comment-sim_grade`, **kwds) -> `_Tnamedtuple-FSimilar-name-comment-sim_grade`: ...
