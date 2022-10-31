from typing import Any

class ThreadStillRunningError(Exception): ...

class PyFrcPlugin:
    robot_class: Any = ...
    _robot_file: Any = ...
    _robot_path: Any = ...
    _fake_time: Any = ...
    _control: Any = ...
    _started: bool = ...
    def __init__(self, robot_class: Any, robot_file: Any, robot_path: Any) -> None: ...
    _test_controller: Any = ...
    def pytest_runtest_setup(self): ...
    def pytest_runtest_teardown(self, nextitem: Any) -> None: ...
    def control(self): ...
    def fake_time(self): ...
    def hal_data(self): ...
    def robot(self): ...
    def robot_file(self): ...
    def robot_path(self): ...
    def wpilib(self): ...
    def get_control(self): ...
    def get_fake_time(self): ...
    def get_robot(self): ...