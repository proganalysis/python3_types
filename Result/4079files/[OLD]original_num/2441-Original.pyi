# (generated with --quick)

import steam_vr_wheel._virtualpad
from typing import Any, Optional, SupportsFloat, Type

LeftTrackpadAxisDisablerMixin: Type[steam_vr_wheel._virtualpad.LeftTrackpadAxisDisablerMixin]
VirtualPad: Type[steam_vr_wheel._virtualpad.VirtualPad]
Wheel: Any

class TouchWheel(steam_vr_wheel._virtualpad.LeftTrackpadAxisDisablerMixin, Any):
    trackpadLX: Any
    trackpadLY: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def _get_touch_angle(self, ctr) -> Optional[float]: ...
    def update(self, left_ctr, right_ctr) -> None: ...

def atan2(__y: SupportsFloat, __x: SupportsFloat) -> float: ...
