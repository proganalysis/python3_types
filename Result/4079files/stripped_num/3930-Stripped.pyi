# (generated with --quick)

from typing import Any, Callable, Dict, Tuple

bind_unused_port: Any
contextlib: module
ignore_deprecation: Callable[..., contextlib._GeneratorContextManager]
os: module
platform: module
skipIfNoIPv6: Callable[[Callable], Callable]
skipIfNoNetwork: Callable[[Callable], Callable]
skipIfNonUnix: Callable[[Callable], Callable]
skipNotCPython: Callable[[Callable], Callable]
skipOnTravis: Callable[[Callable], Callable]
skipPypy3V58: Callable[[Callable], Callable]
socket: module
sys: module
textwrap: module
typing: module
unittest: module
warnings: module

def _detect_ipv6() -> bool: ...
def exec_test(caller_globals, caller_locals, s) -> Dict[str, Any]: ...
def refusing_port() -> Tuple[Callable[[], None], Any]: ...
def subTest(test, *args, **kwargs) -> Any: ...
