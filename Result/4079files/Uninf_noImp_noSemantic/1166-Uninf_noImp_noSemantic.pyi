def test_simple() -> None: ...

class Dummy:
    def method(self) -> None: ...
    @classmethod
    def class_method(cls) -> None: ...
    @staticmethod
    def static_method() -> None: ...

class DummyChild(Dummy):
    def class_method(self) -> None: ...

def test_is_static() -> None: ...
