from typing import Any
from unittest import TestCase

corpus: Any

class LabeledExampleTest(TestCase):
    def test(self) -> None: ...
    def test_serialize_positional_label(self) -> None: ...
