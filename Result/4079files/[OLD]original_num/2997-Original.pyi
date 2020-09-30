# (generated with --quick)

from typing import Any, Callable, Optional, Tuple

__all__: Tuple[str]
abc: module
doctest: module
functools: module
typing: module

class BaseDecorator(metaclass=abc.ABCMeta):
    _BaseDecorator__func: Optional[Callable]
    __doc__: str
    _func: Optional[Callable]
    def __call__(self, *args, **kwargs) -> Any: ...
    def __init__(self, func: Optional[Callable] = ...) -> None: ...
    def __repr__(self) -> str: ...
    @abstractmethod
    def _get_function_wrapper(self, func: Callable) -> Callable: ...
