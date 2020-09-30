# (generated with --quick)

import steam_vr_wheel._virtualpad
from typing import Any, Type

HID_USAGE_RX: Any
HID_USAGE_RY: Any
HID_USAGE_RZ: Any
HID_USAGE_X: Any
HID_USAGE_Y: Any
HID_USAGE_Z: Any
LeftTrackpadAxisDisablerMixin: Type[steam_vr_wheel._virtualpad.LeftTrackpadAxisDisablerMixin]
RightTrackpadAxisDisablerMixin: Type[steam_vr_wheel._virtualpad.RightTrackpadAxisDisablerMixin]
VirtualPad: Type[steam_vr_wheel._virtualpad.VirtualPad]
openvr: Any

class Joystick(steam_vr_wheel._virtualpad.RightTrackpadAxisDisablerMixin, steam_vr_wheel._virtualpad.LeftTrackpadAxisDisablerMixin, steam_vr_wheel._virtualpad.VirtualPad):
    grabbable_x: Throttle
    grabbable_y: Throttle
    grabbable_z: Throttle
    joystick_grabbed: Any
    throttle_x: Throttle
    throttle_y: Throttle
    throttle_z: Throttle
    x: int
    y: int
    def _update_grabbable_joystick(self, axisX, axisY, axisZ) -> None: ...
    def _update_joystick_normal(self, axisX, axisY, axisZ) -> None: ...
    def update(self, left_ctr, right_ctr) -> None: ...

class Throttle:
    invertion: int
    size: Any
    throttle_at_real_world_z: Any
    throttle_grabbed: bool
    throttle_real_world_z: Any
    throttle_relative_zeroed: bool
    throttle_z: Any
    x: Any
    def __init__(self, size = ..., inverted = ..., starting = ...) -> None: ...
    def grabbed(self) -> None: ...
    def ungrabbed(self) -> None: ...
    def update(self, value) -> None: ...
