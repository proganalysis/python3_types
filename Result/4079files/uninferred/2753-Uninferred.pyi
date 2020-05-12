import unittest

class TestPrettyRepr(unittest.TestCase):
    def test_simple(self) -> None: ...
    def test_text(self) -> None: ...
    def test_iterable(self) -> None: ...
    def test_dict(self) -> None: ...
    def test_nested_obj(self) -> None: ...
    def test_callable(self) -> None: ...
    def test_indent(self) -> None: ...
    def test_magic_override(self): ...

class TestAnnotated(unittest.TestCase):
    def test_001_annotation_args(self) -> None: ...
    def test_002_annotation_return(self) -> None: ...
    def test_003_complex(self) -> None: ...
