# (generated with --quick)

import contextlib
from typing import Any, Callable, Iterator, TypeVar

attestation_swig: Any
remote_attestation_context: Callable[..., contextlib._GeneratorContextManager]

_T = TypeVar('_T')

def __getattr__(name) -> Any: ...
def contextmanager(func: Callable[..., Iterator[_T]]) -> Callable[..., contextlib._GeneratorContextManager[_T]]: ...
def initialize_remote_attestation(challenger_public_key, use_pse = ...) -> Any: ...
