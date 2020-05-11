# (generated with --quick)

from typing import Any, Dict, Generator

importlib: module
inspect: module
os: module

class ViewRegistrant:
    f: Any
    next: Any
    options: Any
    route: Any
    def RegisterInFlask(self, app) -> None: ...
    def __call__(self, *args, **kwargs) -> Any: ...
    def __init__(self, f, route, options) -> None: ...

class ViewRegistrar:
    options: Dict[str, Any]
    route: Any
    def __call__(self, f) -> ViewRegistrant: ...
    def __init__(self, route, **options) -> None: ...

class ViewRegistry:
    registrants: list
    def RegisterInFlask(self, app) -> None: ...
    def __init__(self, pkgname, pkgfile) -> None: ...

def _enumerate_modules(pkgname, pkgfile) -> Generator[module, Any, None]: ...
