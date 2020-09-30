# (generated with --quick)

from typing import Any, Optional, Tuple, Type

BaseEvent: Any
ChromeTypeBase: Any
PayloadMixin: Any
PermissionType: Type[str]
WindowID: Type[int]
WindowState: Type[str]
log: Any
logging: Any

class Bounds(Any):
    height: Any
    left: Any
    top: Any
    width: Any
    windowState: Any
    def __init__(self, left: Optional[int] = ..., top: Optional[int] = ..., width: Optional[int] = ..., height: Optional[int] = ..., windowState: Optional[str] = ...) -> None: ...

class Browser(Any):
    __doc__: str
    @classmethod
    def close(cls) -> Tuple[Any, None]: ...
    @classmethod
    def crash(cls) -> Tuple[Any, None]: ...
    @classmethod
    def crashGpuProcess(cls) -> Tuple[Any, None]: ...
    @classmethod
    def getBrowserCommandLine(cls) -> Tuple[Any, Any]: ...
    @classmethod
    def getHistogram(cls, name: str, delta: bool = ...) -> Tuple[Any, Any]: ...
    @classmethod
    def getHistograms(cls, query: Optional[str] = ..., delta: bool = ...) -> Tuple[Any, Any]: ...
    @classmethod
    def getVersion(cls) -> Tuple[Any, Any]: ...
    @classmethod
    def getWindowBounds(cls, windowId: int) -> Tuple[Any, Any]: ...
    @classmethod
    def getWindowForTarget(cls, targetId = ...) -> Tuple[Any, Any]: ...
    @classmethod
    def grantPermissions(cls, origin: str, permissions, browserContextId = ...) -> Tuple[Any, None]: ...
    @classmethod
    def resetPermissions(cls, browserContextId = ...) -> Tuple[Any, None]: ...
    @classmethod
    def setDockTile(cls, badgeLabel: Optional[str] = ..., image: Optional[str] = ...) -> Tuple[Any, None]: ...
    @classmethod
    def setWindowBounds(cls, windowId: int, bounds: Bounds) -> Tuple[Any, None]: ...

class Bucket(Any):
    count: int
    high: int
    low: int
    def __init__(self, low: int, high: int, count: int) -> None: ...

class Histogram(Any):
    buckets: Any
    count: int
    name: str
    sum: int
    def __init__(self, name: str, sum: int, count: int, buckets) -> None: ...
