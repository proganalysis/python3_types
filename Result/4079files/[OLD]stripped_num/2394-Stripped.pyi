# (generated with --quick)

from typing import Any
import unittest.case

PYTHON3: bool
SocketIO: Any
backend: Any
send: Any
socketio: Any
sys: module
unittest: module

class Test(unittest.case.TestCase):
    app: Any
    def test_load_main_page(self) -> None: ...

class TestSocketError(unittest.case.TestCase):
    def test_same_port(self) -> None: ...

class TestWebsockets(unittest.case.TestCase):
    @classmethod
    def setUp(self) -> None: ...
    def test_connect(self) -> None: ...

def main() -> int: ...
