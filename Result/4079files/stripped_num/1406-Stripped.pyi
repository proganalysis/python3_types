# (generated with --quick)

from typing import Any, NoReturn

MagicMock: Any
MonitoredSwitchChange: Any
MpfTestCase: Any

class TestSwitchController(Any):
    called1: int
    called2: int
    called3: int
    isActive: Any
    def _callback(self, state, ms, switch_name) -> None: ...
    def _callback_invalid(self) -> NoReturn: ...
    def _cb1a(self, **kwargs) -> None: ...
    def _cb1b(self, **kwargs) -> None: ...
    def _cb2(self, **kwargs) -> None: ...
    def _cb3(self, **kwargs) -> None: ...
    def getConfigFile(self) -> str: ...
    def getMachinePath(self) -> str: ...
    def test_activation_and_deactivation_events(self) -> None: ...
    def test_active_and_inactive_times(self) -> None: ...
    def test_ignore_window_ms(self) -> None: ...
    def test_initial_state(self) -> None: ...
    def test_invert(self) -> None: ...
    def test_is_active_timing(self) -> None: ...
    def test_monitor(self) -> None: ...
    def test_remove_in_handler(self) -> None: ...
    def test_remove_in_handler2(self) -> None: ...
    def test_timed_switch_handler(self) -> None: ...
    def test_verify_switches(self) -> None: ...
    def test_wait_futures(self) -> None: ...
