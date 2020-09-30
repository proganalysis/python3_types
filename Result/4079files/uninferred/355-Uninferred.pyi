from typing import Any

__author__: str

class Singleton(type):
    _instances: Any = ...
    def __call__(cls, *args: Any, **kwargs: Any): ...
