import unittest
from typing import Any

def _Detect(test: Any, word_str: Any, expected: Any) -> None: ...

class WordTest(unittest.TestCase):
    def testDetectLocation(self) -> None: ...
