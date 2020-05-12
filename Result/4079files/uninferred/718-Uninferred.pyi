from overloading import *
from test_overloading import *
from typing import Any

class B:
    def f(cls, foo: Any, bar: Any): ...

class C:
    @classmethod
    def f(cls, foo: Any, bar: Any): ...

class D:
    @classmethod
    def f(cls, foo: Any, bar: Any): ...
