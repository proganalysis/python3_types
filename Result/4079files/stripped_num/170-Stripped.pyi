# (generated with --quick)

from typing import Any, Dict, List, Tuple

CMake: Any
ConanException: Any
ConanFile: Any

class OpenrwConan(Any):
    _rw_dependencies: Dict[str, Tuple[str, ...]]
    default_options: Tuple[str, str, str, str, str]
    description: str
    exports_sources: Tuple[str, str, str, str, str, str, str, str, str, str, str]
    generators: Tuple[str]
    license: str
    name: str
    options: Dict[str, List[bool]]
    settings: Tuple[str, str, str, str]
    url: str
    version: str
    def _configure_cmake(self) -> Any: ...
    def build(self) -> None: ...
    def configure(self) -> None: ...
    def package(self) -> None: ...
    def package_info(self) -> None: ...
    def requirements(self) -> None: ...
