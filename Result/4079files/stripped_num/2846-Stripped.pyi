# (generated with --quick)

from typing import Any, Tuple, Type

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
    def __init__(self, left = ..., top = ..., width = ..., height = ..., windowState = ...) -> None: ...

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
    def getHistogram(cls, name, delta = ...) -> Tuple[Any, Any]: ...
    @classmethod
    def getHistograms(cls, query = ..., delta = ...) -> Tuple[Any, Any]: ...
    @classmethod
    def getVersion(cls) -> Tuple[Any, Any]: ...
    @classmethod
    def getWindowBounds(cls, windowId) -> Tuple[Any, Any]: ...
    @classmethod
    def getWindowForTarget(cls, targetId = ...) -> Tuple[Any, Any]: ...
    @classmethod
    def grantPermissions(cls, origin, permissions, browserContextId = ...) -> Tuple[Any, None]: ...
    @classmethod
    def resetPermissions(cls, browserContextId = ...) -> Tuple[Any, None]: ...
    @classmethod
    def setDockTile(cls, badgeLabel = ..., image = ...) -> Tuple[Any, None]: ...
    @classmethod
    def setWindowBounds(cls, windowId, bounds) -> Tuple[Any, None]: ...

class Bucket(Any):
    count: Any
    high: Any
    low: Any
    def __init__(self, low, high, count) -> None: ...

class Histogram(Any):
    buckets: Any
    count: Any
    name: Any
    sum: Any
    def __init__(self, name, sum, count, buckets) -> None: ...
