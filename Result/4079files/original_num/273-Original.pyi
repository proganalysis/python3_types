# (generated with --quick)

from typing import Any, Optional, Tuple, Type

BaseEvent: Any
ChromeTypeBase: Any
ImageType: Type[str]
PayloadMixin: Any
SubsamplingFormat: Type[str]
log: Any
logging: Any

class GPUDevice(Any):
    deviceId: float
    deviceString: str
    driverVendor: str
    driverVersion: str
    vendorId: float
    vendorString: str
    def __init__(self, vendorId: float, deviceId: float, vendorString: str, deviceString: str, driverVendor: str, driverVersion: str) -> None: ...

class GPUInfo(Any):
    auxAttributes: Optional[dict]
    devices: Any
    driverBugWorkarounds: Any
    featureStatus: Optional[dict]
    imageDecoding: Any
    videoDecoding: Any
    videoEncoding: Any
    def __init__(self, devices, driverBugWorkarounds, videoDecoding, videoEncoding, imageDecoding, auxAttributes: Optional[dict] = ..., featureStatus: Optional[dict] = ...) -> None: ...

class ImageDecodeAcceleratorCapability(Any):
    imageType: str
    maxDimensions: Size
    minDimensions: Size
    subsamplings: Any
    def __init__(self, imageType: str, maxDimensions: Size, minDimensions: Size, subsamplings) -> None: ...

class ProcessInfo(Any):
    cpuTime: float
    id: int
    type: str
    def __init__(self, type: str, id: int, cpuTime: float) -> None: ...

class Size(Any):
    height: int
    width: int
    def __init__(self, width: int, height: int) -> None: ...

class SystemInfo(Any):
    __doc__: str
    @classmethod
    def getInfo(cls) -> Tuple[Any, Any]: ...
    @classmethod
    def getProcessInfo(cls) -> Tuple[Any, Any]: ...

class VideoDecodeAcceleratorCapability(Any):
    maxResolution: Size
    minResolution: Size
    profile: str
    def __init__(self, profile: str, maxResolution: Size, minResolution: Size) -> None: ...

class VideoEncodeAcceleratorCapability(Any):
    maxFramerateDenominator: int
    maxFramerateNumerator: int
    maxResolution: Size
    profile: str
    def __init__(self, profile: str, maxResolution: Size, maxFramerateNumerator: int, maxFramerateDenominator: int) -> None: ...
