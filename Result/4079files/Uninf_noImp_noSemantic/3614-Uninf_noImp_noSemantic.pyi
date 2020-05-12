from datetime import datetime as datetime
from typing import Any

def create_with_state(state: Any): ...
def create_with_description(description: Any): ...

class TestStatus:
    def test_from_dict(self) -> None: ...
    def test_pending(self, test_input: Any, expected: Any) -> None: ...
    def test_succeeded(self, test_input: Any, expected: Any) -> None: ...
    def test_failed(self, test_input: Any, expected: Any) -> None: ...
    def test_taken(self, test_input: Any, expected: Any) -> None: ...
    def test_rerun_pending(self, test_input: Any, expected: Any) -> None: ...
    def test_unassigned(self, test_input: Any, expected: Any) -> None: ...
