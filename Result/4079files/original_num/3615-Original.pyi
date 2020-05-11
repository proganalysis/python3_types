# (generated with --quick)

import contextlib
from typing import Any, Callable, Iterator, TypeVar

SchrootChroot: Any
os: module
select: module
spark_schroot: Callable[..., contextlib._GeneratorContextManager]
subprocess: module
time: module

_T = TypeVar('_T')

def chroot_copy(chroot, what, whence, user = ...) -> None: ...
def chroot_run_logged(schroot, jlog, cmd, **kwargs) -> Any: ...
def chroot_upgrade(chroot, jlog) -> bool: ...
def contextmanager(func: Callable[..., Iterator[_T]]) -> Callable[..., contextlib._GeneratorContextManager[_T]]: ...
