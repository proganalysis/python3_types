# (generated with --quick)

import __future__
from typing import Any, Tuple

CamJamKitRobot: Any
ControllerResource: Any
division: __future__._Feature
joystick: Any
motor_left: Any
motor_multiplier: int
motor_right: Any
power_left: int
power_right: int
robot: Any
x_axis: Any
y_axis: Any

class RobotStopException(Exception):
    __doc__: str

def mixer(yaw, throttle, max_power = ...) -> Tuple[int, int]: ...
def set_speeds(power_left, power_right) -> None: ...
def sleep(secs: float) -> None: ...
def stop_motors() -> None: ...
