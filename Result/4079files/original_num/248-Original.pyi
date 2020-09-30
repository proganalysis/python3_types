# (generated with --quick)

from typing import Any, Iterable, Iterator, Optional

itertools: module
models: Any
os: module
utils: Any

class ContainerOptions:
    DEFAULT_PYPATH_DIR: str
    DEFAULT_SRC_DIR: str
    __doc__: str
    _command: Optional[str]
    _container_source_directory: str
    _environment_variables: Iterable
    _ext_volumes: Iterable
    _image: str
    _network: Optional[str]
    _ports: Iterable
    _py_volumes: Iterable[str]
    _pypath_directory: str
    _remove_container: bool
    _source_directory: str
    command: Optional[str]
    image: str
    network: Optional[str]
    remove_container: bool
    def __init__(self, image: str, source_directory: str, *, command: Optional[str] = ..., container_source_directory: str = ..., environment_variables: Optional[Iterable] = ..., ext_volumes: Optional[Iterable] = ..., network: Optional[str] = ..., py_volumes: Optional[Iterable[str]] = ..., ports: Optional[Iterable] = ..., pypath_directory: str = ..., remove_container: bool = ...) -> None: ...
    def get_environment_collection(self) -> list: ...
    def get_ports(self) -> list: ...
    def get_pythonpath_environment(self) -> Any: ...
    def get_source_volume(self) -> Any: ...
    def get_volume_collection(self) -> list: ...
    def iter_environment_variables(self) -> Iterator: ...
    def iter_ext_volumes(self) -> Iterator: ...
    def iter_pypath_volumes(self) -> Iterator: ...
