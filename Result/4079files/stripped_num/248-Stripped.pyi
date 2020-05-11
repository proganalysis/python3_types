# (generated with --quick)

from typing import Any, Generator, Iterable, Iterator

itertools: module
models: Any
os: module
utils: Any

class ContainerOptions:
    DEFAULT_PYPATH_DIR: str
    DEFAULT_SRC_DIR: str
    __doc__: str
    _command: Any
    _container_source_directory: Any
    _environment_variables: Iterable
    _ext_volumes: Iterable
    _image: Any
    _network: Any
    _ports: Iterable
    _py_volumes: Iterable[str]
    _pypath_directory: Any
    _remove_container: Any
    _source_directory: Any
    command: Any
    image: Any
    network: Any
    remove_container: Any
    def __init__(self, image, source_directory, *, command = ..., container_source_directory = ..., environment_variables = ..., ext_volumes = ..., network = ..., py_volumes = ..., ports = ..., pypath_directory = ..., remove_container = ...) -> None: ...
    def get_environment_collection(self) -> list: ...
    def get_ports(self) -> list: ...
    def get_pythonpath_environment(self) -> Any: ...
    def get_source_volume(self) -> Any: ...
    def get_volume_collection(self) -> list: ...
    def iter_environment_variables(self) -> Iterator: ...
    def iter_ext_volumes(self) -> Iterator: ...
    def iter_pypath_volumes(self) -> Generator[Any, Any, None]: ...
