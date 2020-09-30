# (generated with --quick)

from typing import Any, Tuple, Type

BaseEvent: Any
ChromeTypeBase: Any
ImageType: Type[str]
PayloadMixin: Any
SubsamplingFormat: Type[str]
log: Any
logging: Any

class GPUDevice(Any):
    deviceId: Any
    deviceString: Any
    driverVendor: Any
    driverVersion: Any
    vendorId: Any
    vendorString: Any
    def __init__(self, vendorId, deviceId, vendorString, deviceString, driverVendor, driverVersion) -> None: ...

class GPUInfo(Any):
    auxAttributes: Any
    devices: Any
    driverBugWorkarounds: Any
    featureStatus: Any
    imageDecoding: Any
    videoDecoding: Any
    videoEncoding: Any
    def __init__(self, devices, driverBugWorkarounds, videoDecoding, videoEncoding, imageDecoding, auxAttributes = ..., featureStatus = ...) -> None: ...

class ImageDecodeAcceleratorCapability(Any):
    imageType: Any
    maxDimensions: Any
    minDimensions: Any
    subsamplings: Any
    def __init__(self, imageType, maxDimensions, minDimensions, subsamplings) -> None: ...

class ProcessInfo(Any):
    cpuTime: Any
    id: Any
    type: Any
    def __init__(self, type, id, cpuTime) -> None: ...

class Size(Any):
    height: Any
    width: Any
    def __init__(self, width, height) -> None: ...

class SystemInfo(Any):
    __doc__: str
    @classmethod
    def getInfo(cls) -> Tuple[Any, Any]: ...
    @classmethod
    def getProcessInfo(cls) -> Tuple[Any, Any]: ...

class VideoDecodeAcceleratorCapability(Any):
    maxResolution: Any
    minResolution: Any
    profile: Any
    def __init__(self, profile, maxResolution, minResolution) -> None: ...

class VideoEncodeAcceleratorCapability(Any):
    maxFramerateDenominator: Any
    maxFramerateNumerator: Any
    maxResolution: Any
    profile: Any
    def __init__(self, profile, maxResolution, maxFramerateNumerator, maxFramerateDenominator) -> None: ...
