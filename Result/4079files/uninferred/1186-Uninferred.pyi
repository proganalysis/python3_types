from chromewhip.helpers import BaseEvent as BaseEvent, ChromeTypeBase as ChromeTypeBase, PayloadMixin
from typing import Any, Union

log: Any

class DeviceOrientation(PayloadMixin):
    @classmethod
    def clearDeviceOrientationOverride(cls): ...
    @classmethod
    def setDeviceOrientationOverride(cls: Any, alpha: Union[float], beta: Union[float], gamma: Union[float]) -> Any: ...
