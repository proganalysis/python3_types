# (generated with --quick)

import queue
from typing import Any, Iterable, Iterator, List, Tuple, Type

CommandMsg: Any
JointState: Any
MotionMsg: Any
MotionSmoother: Any
MovementMsg: Any
Queue: Type[queue.Queue]
argparse: module
args: argparse.Namespace
logging: module
motion_controller: MotionController
rospy: Any
show_plot: Any
sys: module
time: module

class MotionController:
    _MotionController__motion_smoother: Any
    _MotionController__rate: Any
    _MotionController__roc_command_queue: queue.Queue[nothing]
    __doc__: str
    joint_command_pin_publisher: Any
    joint_command_publisher: Any
    roc_command_subscriber: Any
    def __init__(self, show_plot = ..., refresh_rate = ...) -> None: ...
    def get_all_joint_names_in_roc_command(self, roc_command) -> list: ...
    def get_current_joint_positions(self) -> list: ...
    def get_data_point_for_roc_command(self, current_joint_positions, roc_command) -> List[List[Tuple[Any, Any, Any]]]: ...
    def get_joint_pins_from_names(self, joint_pin_dict, joint_names) -> list: ...
    def get_movemnent_list(self, roc_command) -> List[List[Tuple[Any, Any, Any]]]: ...
    def get_relevant_current_positions(self, current_joint_positions, roc_commands) -> List[Tuple[Any, Any, Any]]: ...
    def roc_command_callback(self, data) -> None: ...
    def run(self) -> None: ...

def get_cmd_args(args) -> argparse.Namespace: ...
def zip_longest(*p: Iterable, fillvalue = ...) -> Iterator: ...
