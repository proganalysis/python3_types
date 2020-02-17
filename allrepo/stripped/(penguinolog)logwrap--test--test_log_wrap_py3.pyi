# (generated with --quick)

from typing import Any
import unittest.case

asyncio: module
io: module
logging: module
logwrap: Any
mock: module
typing: module
unittest: module

class TestAnnotated(unittest.case.TestCase):
    logger: logging.Logger
    stream: io.StringIO
    def test_annotation_args(self) -> None: ...

class TestLogWrapAsync(unittest.case.TestCase):
    logger: logging.Logger
    stream: io.StringIO
    @classmethod
    def setUpClass(cls) -> None: ...
    def test_coroutine_async(self) -> None: ...
    def test_coroutine_async_as_argumented(self) -> None: ...
    def test_coroutine_fail(self) -> None: ...
    def test_exceptions_blacklist(self) -> None: ...
