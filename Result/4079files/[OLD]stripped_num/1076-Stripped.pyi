# (generated with --quick)

import functools
from typing import Any, Callable, Optional, TypeVar

json: module
urllib: module

_T = TypeVar('_T')

class PackageRepository:
    __doc__: str
    data: Any
    json_path: Any
    def __init__(self, json_path = ...) -> None: ...
    def _load_json(self) -> Any: ...
    def filter_where(self, package_type, value) -> list: ...
    def get_installed_packages(self) -> list: ...
    def get_properties(self, package_property) -> list: ...
    def get_property(self, package_name, package_property) -> Any: ...
    def get_sources(self, package_name) -> Any: ...

def lru_cache(maxsize: Optional[int] = ..., typed: bool = ...) -> Callable[[Callable[..., _T]], functools._lru_cache_wrapper[_T]]: ...
