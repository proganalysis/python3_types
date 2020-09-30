# (generated with --quick)

from typing import Any

TestController: Any
fake_time: Any
hal_impl: Any
pyfrc_fake_hooks: Any
pytest: Any

class PyFrcPlugin:
    __doc__: str
    _control: None
    _fake_time: Any
    _robot_file: Any
    _robot_path: Any
    _started: bool
    _test_controller: Any
    control: Any
    fake_time: Any
    hal_data: Any
    robot: Any
    robot_file: Any
    robot_path: Any
    wpilib: Any
    def __init__(self, robot_class, robot_file, robot_path) -> None: ...
    def get_control(self) -> Any: ...
    def get_fake_time(self) -> Any: ...
    def get_robot(self) -> Any: ...
    def pytest_runtest_setup(self) -> None: ...
    def pytest_runtest_teardown(self, nextitem) -> None: ...
    def robot_class(self) -> Any: ...

class ThreadStillRunningError(Exception): ...
