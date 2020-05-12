# (generated with --quick)

import collections
import typing
from typing import Any, Dict, Type, TypeVar, Union

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
h5py: Any
loads: typing.Callable
logLevel_dict: Dict[int, int]
logger: logging.Logger
logging: module
mp: module
np: module
os: module
pd: Any
tqdm: Any
traceback: module

DV = TypeVar('DV')
K = TypeVar('K')
K2 = TypeVar('K2')
T = TypeVar('T')
V = TypeVar('V')
V2 = TypeVar('V2')

class Fast5_to_seq_summary:
    __doc__: str
    attrs_grp_dict: Dict[str, Dict[str, str]]
    basecall_id: int
    fast5_dir: str
    fields: Any
    include_path: bool
    max_fast5: int
    seq_summary_fn: str
    threads: int
    verbose_level: Any
    def __init__(self, fast5_dir: str, seq_summary_fn: str, max_fast5: int = ..., threads: int = ..., basecall_id: int = ..., verbose_level = ..., include_path: bool = ..., fields = ...) -> None: ...
    @staticmethod
    def _get_h5_attrs(fp, grp, attrs) -> Any: ...
    def _list_fast5(self, in_q, error_q) -> None: ...
    def _read_fast5(self, in_q, out_q, error_q, counter_q, worker_id) -> None: ...
    def _write_seq_summary(self, out_q, error_q, counter_q) -> None: ...

def __getattr__(name) -> Any: ...
def namedtuple(typename: str, field_names: Union[str, typing.Iterable[str]], *, verbose: bool = ..., rename: bool = ...) -> type: ...
def time() -> float: ...
