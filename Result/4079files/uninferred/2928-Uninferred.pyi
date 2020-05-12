import enum
import single_robot_composite_behavior

class OurPlacement(single_robot_composite_behavior.SingleRobotCompositeBehavior):
    class State(enum.Enum):
        dribble: int = ...
        pause: int = ...
        avoid: int = ...
    pause_time: int = ...
    def __init__(self): ...
    def on_enter_dribble(self) -> None: ...
    def execute_dribble(self) -> None: ...
    def on_exit_dribble(self) -> None: ...
    def on_enter_pause(self) -> None: ...
    def execute_pause(self) -> None: ...
    def execute_avoid(self) -> None: ...
    def role_requirements(self): ...
