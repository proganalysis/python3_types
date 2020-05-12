from .api import API, CustomList
from collections import namedtuple
from typing import Any, Optional

__all__: Any

class ImageAPI(API):
    _serviceType: str = ...
    def __init__(self, token: Any, baseURIPrefix: Optional[Any] = ...) -> None: ...

class Image(ImageAPI):
    status: Any = ...
    name: Any = ...
    tags: Any = ...
    container_format: Any = ...
    created_at: Any = ...
    size: Any = ...
    disk_format: Any = ...
    updated_at: Any = ...
    visibility: Any = ...
    imageId: Any = ...
    min_disk: Any = ...
    protected: Any = ...
    min_ram: Any = ...
    file: Any = ...
    checksum: Any = ...
    owner: Any = ...
    direct_url: Any = ...
    hw_qemu_guest_agent: Any = ...
    schema: Any = ...
    def __init__(self, data: Any) -> None: ...

class ImageList(ImageAPI, CustomList):
    def __init__(self, token: Any) -> None: ...
    def _getitem(self, key: Any, item: Any): ...
    def delete(self, imageId: Any) -> None: ...

class Quota(ImageAPI):

    QuotaTuple = namedtuple('QuotaTuple', ['region', 'size'])
    def __init__(self, token: Any) -> None: ...
    region: Any = ...
    size: Any = ...
    def update(self, res: Optional[Any] = ...) -> None: ...
    def set(self, size: Any) -> None: ...
    @staticmethod
    def _validateSize(size: Any) -> None: ...
