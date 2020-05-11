# (generated with --quick)

import collections
import typing
from typing import Any, List, Type, TypeVar, Union

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
datetime: module
defaultdict: Type[collections.defaultdict]
deque: Type[collections.deque]
dumps: typing.Callable
loads: typing.Callable
np: module
pd: Any
warnings: module

AnyStr = TypeVar('AnyStr', str, bytes)
DV = TypeVar('DV')
K = TypeVar('K')
K2 = TypeVar('K2')
T = TypeVar('T')
V = TypeVar('V')
V2 = TypeVar('V2')
_T0 = TypeVar('_T0')

class pycoQC_parse:
    bam_file_list: Any
    barcode_files_list: Any
    counter: collections.OrderedDict[str, int]
    filter_calibration: Any
    logger: Any
    min_barcode_percent: Any
    run_type: str
    runid_list: Any
    summary_files_list: Any
    def __call__(self) -> Any: ...
    def __init__(self, summary_file, barcode_file = ..., bam_file = ..., runid_list = ..., filter_calibration = ..., min_barcode_percent = ..., verbose = ..., quiet = ...) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> Any: ...
    @staticmethod
    def _check_df_columns(df, required_colnames, optional_colnames) -> list: ...
    def _clean_df(self, df) -> Any: ...
    @staticmethod
    def _expand_file_names(fn: _T0) -> Union[list, _T0]: ...
    @staticmethod
    def _merge_files_to_df(fn_list) -> Any: ...
    def _parse_bam(self, df: _T0) -> _T0: ...
    def _parse_barcode(self, df) -> Any: ...
    def _parse_summary(self) -> Any: ...

def __getattr__(name) -> Any: ...
def glob(pathname: AnyStr, *, recursive: bool = ...) -> List[AnyStr]: ...
def namedtuple(typename: str, field_names: Union[str, typing.Iterable[str]], *, verbose: bool = ..., rename: bool = ...) -> type: ...
