# (generated with --quick)

from typing import Any, List, Optional, Tuple, Type, Union
import unittest.case

ChildMonitor: Any
ConsoleMonitor: Any
Monitor: Any
TestCase: Type[unittest.case.TestCase]
fetch_std_streams: Any

class ChildMonitorTest(unittest.case.TestCase):
    def test_cancel(self) -> None: ...
    def test_child_monitor(self) -> None: ...
    def test_no_label(self) -> None: ...

class ConsoleMonitorTest(unittest.case.TestCase):
    def test_cancel(self) -> None: ...
    def test_child_monitor(self) -> None: ...
    def test_console_monitor_with_progress_bar(self) -> None: ...
    def test_console_monitor_wo_progress_bar(self) -> None: ...
    def test_label_required(self) -> None: ...

class NullMonitorTest(unittest.case.TestCase):
    def test_NONE(self) -> None: ...
    def test_cancel(self) -> None: ...
    def test_child_monitor(self) -> None: ...

class RecordingMonitor(Any):
    __doc__: str
    _cancelled: Optional[bool]
    _label: Optional[str]
    _records: List[Tuple[Optional[Union[float, int, str]], ...]]
    _total_work: Optional[float]
    _worked: Any
    records: Any
    def __init__(self) -> None: ...
    def __str__(self) -> str: ...
    def cancel(self) -> None: ...
    def done(self) -> None: ...
    def is_cancelled(self) -> bool: ...
    def progress(self, work: Optional[float] = ..., msg: Optional[str] = ...) -> None: ...
    def start(self, label: str, total_work: Optional[float] = ...) -> None: ...

class RecordingMonitorTest(unittest.case.TestCase):
    def test_context_manager(self) -> None: ...
    def test_recording_monitor(self) -> None: ...