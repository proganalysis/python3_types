# (generated with --quick)

from typing import Any, Tuple

__all__: Tuple[str]
abc: module
doctest: module
functools: module
typing: module

class BaseDecorator(metaclass=abc.ABCMeta):
    _BaseDecorator__func: Any
    __doc__: str
    _func: Any
    def __call__(self, *args, **kwargs) -> Any: ...
    def __init__(self, func = ...) -> None: ...
    def __repr__(self) -> str: ...
    @abstractmethod
    def _get_function_wrapper(self, func) -> Any: ...
