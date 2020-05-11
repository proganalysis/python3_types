# (generated with --quick)

import collections
from typing import Any, Callable, Iterable, List, Sized, Tuple, Type, TypeVar, Union

API: Any
CustomList: Any
__all__: List[str]
error: Any

_Tnamedtuple-QuotaTuple-region-size = TypeVar('_Tnamedtuple-QuotaTuple-region-size', bound=`namedtuple-QuotaTuple-region-size`)

class Image(ImageAPI):
    __doc__: str
    checksum: Any
    container_format: Any
    created_at: Any
    direct_url: Any
    disk_format: Any
    file: Any
    hw_qemu_guest_agent: Any
    imageId: Any
    min_disk: Any
    min_ram: Any
    name: Any
    owner: Any
    protected: Any
    schema: Any
    size: Any
    status: Any
    tags: Any
    updated_at: Any
    visibility: Any
    def __init__(self, data) -> None: ...

class ImageAPI(Any):
    _serviceType: str
    def __init__(self, token, baseURIPrefix = ...) -> None: ...

class ImageList(ImageAPI, Any):
    __doc__: str
    _serviceType: str
    def __init__(self, token) -> None: ...
    def _getitem(self, key, item) -> bool: ...
    def delete(self, imageId) -> None: ...

class Quota(ImageAPI):
    QuotaTuple: Type[`namedtuple-QuotaTuple-region-size`]
    __doc__: str
    _serviceType: str
    region: Any
    size: int
    def __init__(self, token) -> None: ...
    @staticmethod
    def _validateSize(size) -> None: ...
    def set(self, size) -> None: ...
    def update(self, res = ...) -> None: ...

class `namedtuple-QuotaTuple-region-size`(tuple):
    __slots__ = ["region", "size"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str]
    region: Any
    size: Any
    def __getnewargs__(self) -> Tuple[Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-QuotaTuple-region-size`], region, size) -> `_Tnamedtuple-QuotaTuple-region-size`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-QuotaTuple-region-size`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-QuotaTuple-region-size`: ...
    def _replace(self: `_Tnamedtuple-QuotaTuple-region-size`, **kwds) -> `_Tnamedtuple-QuotaTuple-region-size`: ...

def namedtuple(typename: str, field_names: Union[str, Iterable[str]], *, verbose: bool = ..., rename: bool = ...) -> type: ...
