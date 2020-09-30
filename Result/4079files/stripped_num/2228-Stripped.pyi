# (generated with --quick)

import contextlib
from typing import Any, Callable, Iterator, TypeVar

assert_that: Any
check_no_warnings: Callable[..., contextlib._GeneratorContextManager]
check_warning: Callable[..., contextlib._GeneratorContextManager]
contains_string: Any
empty: Any
equal_to: Any
has_length: Any
is_: Any
warnings: module

_T = TypeVar('_T')

def check_requirements_exactly_one_warning() -> contextlib._GeneratorContextManager: ...
def check_unsupported_arg_warning() -> contextlib._GeneratorContextManager: ...
def contextmanager(func: Callable[..., Iterator[_T]]) -> Callable[..., contextlib._GeneratorContextManager[_T]]: ...
