# (generated with --quick)

from typing import Any, Dict, Generator, Tuple

LOGGER: Any
MODULE_DIR: str
Project: Any
VERSION_FILE: str
const: Any
glob: module
hashlib: module
imp: Any
inspect: Any
logging: Any
os: Any
pkg_resources: Any
types: Any

class CodeLoader(object):
    _CodeLoader__code_dir: Any
    _CodeLoader__modules: Dict[Any, Tuple[Any, Any]]
    __doc__: str
    def _CodeLoader__check_dir(self) -> None: ...
    def __init__(self, code_dir) -> None: ...
    def _load_module(self, mod_name, python_file, hv) -> None: ...
    def deploy_version(self, hash_value, module_name, module_source) -> None: ...
    def load_modules(self) -> None: ...

class CodeManager(object):
    _CodeManager__file_info: Dict[Any, SourceInfo]
    _CodeManager__type_file: Dict[Any, set]
    __doc__: str
    def get_file_content(self, hash) -> Any: ...
    def get_file_hashes(self) -> Generator[nothing, Any, None]: ...
    def get_object_source(self, instance) -> Any: ...
    def get_types(self) -> Generator[Tuple[nothing, Any], Any, None]: ...
    def register_code(self, type_name, instance) -> None: ...

class SourceInfo(object):
    __doc__: str
    _content: None
    _hash: None
    _requires: None
    content: Any
    hash: Any
    module_name: Any
    path: Any
    requires: Any
    def __init__(self, path, module_name) -> None: ...
    def _get_module_name(self) -> Any: ...

class SourceNotFoundException(Exception):
    __doc__: str
