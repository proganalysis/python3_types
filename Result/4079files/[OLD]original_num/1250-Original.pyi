# (generated with --quick)

import collections
import typing
from typing import Any, List, Optional, Type, TypeVar, Union

AsyncGenerator: Type[asyncgenerator]
AsyncIterable: Type[typing.AsyncIterable]
AsyncIterator: Type[typing.AsyncIterator]
Awaitable: Type[typing.Awaitable]
ByteString: Type[typing.ByteString]
Callable: Type[typing.Callable]
ChainMap: Type[typing.ChainMap]
Collection: Type[typing.Collection]
Container: Type[typing.Container]
Coroutine: Type[coroutine]
Counter: Type[typing.Counter]
Generator: Type[generator]
Hashable: Type[typing.Hashable]
ItemsView: Type[typing.ItemsView]
Iterable: Type[typing.Iterable]
Iterator: Type[typing.Iterator]
KeysView: Type[typing.KeysView]
Mapping: Type[typing.Mapping]
MappingView: Type[typing.MappingView]
MutableMapping: Type[typing.MutableMapping]
MutableSequence: Type[typing.MutableSequence]
MutableSet: Type[typing.MutableSet]
OrderedDict: Type[collections.OrderedDict]
R_OK: int
Reversible: Type[typing.Reversible]
Sequence: Type[typing.Sequence]
Set: Type[set]
Sized: Type[typing.Sized]
UserDict: Any
UserList: Any
UserString: Any
ValuesView: Type[typing.ValuesView]
defaultdict: Type[collections.defaultdict]
deque: Type[collections.deque]
dumps: typing.Callable
inspect: module
loads: typing.Callable
logging: module
path: module
pd: Any
sys: module

AnyStr = TypeVar('AnyStr', str, bytes)
DV = TypeVar('DV')
K = TypeVar('K')
K2 = TypeVar('K2')
T = TypeVar('T')
V = TypeVar('V')
V2 = TypeVar('V2')

class pycoQCError(Exception):
    __doc__: str

class pycoQCWarning(Warning):
    __doc__: str

def access(path: Union[_PathLike, bytes, int, str], mode: int, *, dir_fd: Optional[int] = ..., effective_ids: bool = ..., follow_symlinks: bool = ...) -> bool: ...
def arg_opt(func, arg, **kwargs) -> collections.OrderedDict[str, Any]: ...
def check_arg(arg_name, arg_val, required_type, allow_none = ..., min = ..., max = ..., choices = ...) -> Any: ...
def dict_to_str(c, prefix = ..., suffix = ...) -> str: ...
def doc_func(func) -> str: ...
def get_logger(name = ..., verbose = ..., quiet = ...) -> logging.Logger: ...
def glob(pathname: AnyStr, *, recursive: bool = ...) -> List[AnyStr]: ...
def head(fp, n = ..., sep = ..., comment = ...) -> Any: ...
def iglob(pathname: AnyStr, *, recursive: bool = ...) -> typing.Iterator[AnyStr]: ...
def is_readable_file(fn) -> bool: ...
def jhelp(f) -> None: ...
@overload
def listdir(path: bytes) -> List[bytes]: ...
@overload
def listdir(path: Optional[str] = ...) -> List[str]: ...
@overload
def listdir(path: Union[int, _PathLike[str]]) -> List[str]: ...
def make_arg_dict(func) -> Optional[collections.OrderedDict[str, collections.OrderedDict[str, Any]]]: ...
def namedtuple(typename: str, field_names: Union[str, typing.Iterable[str]], *, verbose: bool = ..., rename: bool = ...) -> type: ...
def recursive_file_gen(dir, ext) -> typing.Generator[Any, Any, None]: ...
def sequencing_summary_file_sample(infile, outfile = ..., n_seq = ...) -> Any: ...
