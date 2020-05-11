# (generated with --quick)

import lib.vision_cube
from typing import Any, Coroutine, Optional, Type, Union

BLUE: Any
CustomObject: Any
CustomObjectMarkers: Any
CustomObjectTypes: Any
DEBUG_MODE: bool
GREEN: Any
IP_ADDRESS: Any
ORANGE: Any
PINK: Any
PORT: Any
PURPLE: Any
Pose: Any
USE_LOGGING: bool
USE_VIEWER: bool
VisionCube: Type[lib.vision_cube.VisionCube]
YELLOW: Any
asyncio: module
cozmo: Any
cozmoAction: TapCube
degrees: Any
distance_mm: Any
random: module
serverT: Optional[threading.Thread]
socket: module
speed_mmps: Any
stopFlag: bool
sys: module
threading: module
time: module

class TapCube(threading.Thread):
    _animation_triggered: bool
    _cube: Any
    _did_cozmo_tap_flag: bool
    _message: Union[bytes, str]
    _robot: Any
    _round: int
    _tap_action_finished: bool
    _trigger_message: bool
    _wait_for_tap_flag: bool
    sock: socket.socket
    def __init__(self) -> None: ...
    def coz_tap(self, cube) -> Coroutine[Any, Any, None]: ...
    def find_cube(self) -> Coroutine[Any, Any, Optional[bool]]: ...
    def go_back_to_normal(self) -> Coroutine[Any, Any, None]: ...
    def go_to_cube(self, cube) -> Coroutine[Any, Any, None]: ...
    def on_object_tapped(self, evt = ..., obj = ..., tap_count = ..., **kwargs) -> Coroutine[Any, Any, None]: ...
    def run(self, coz_conn) -> coroutine: ...
    def run_server(self) -> None: ...
    def see_fireworks(self, cube) -> Coroutine[Any, Any, None]: ...
    def send_msg(self, msg) -> None: ...
    def set_up_cozmo(self, coz_conn) -> Coroutine[Any, Any, nothing]: ...
    def trigger_cozmo_tap(self) -> None: ...
