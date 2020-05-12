from typing import Any

robot: Any
motor_left: Any
motor_right: Any
motor_multiplier: int

def set_speeds(power_left: Any, power_right: Any) -> None: ...
def stop_motors() -> None: ...

class RobotStopException(Exception): ...

def mixer(yaw: Any, throttle: Any, max_power: int = ...): ...

x_axis: Any
y_axis: Any
power_left: Any
power_right: Any
