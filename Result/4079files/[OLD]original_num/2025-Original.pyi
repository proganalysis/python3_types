# (generated with --quick)

from typing import Any, Dict, Iterable, List, Optional, Tuple

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
    _CodeLoader__code_dir: str
    _CodeLoader__modules: Dict[str, Tuple[str, Any]]
    __doc__: str
    def _CodeLoader__check_dir(self) -> None: ...
    def __init__(self, code_dir: str) -> None: ...
    def _load_module(self, mod_name: str, python_file: str, hv: str) -> None: ...
    def deploy_version(self, hash_value: str, module_name: str, module_source: str) -> None: ...
    def load_modules(self) -> None: ...

class CodeManager(object):
    _CodeManager__file_info: Dict[Any, SourceInfo]
    _CodeManager__type_file: Dict[str, set]
    __doc__: str
    def get_file_content(self, hash: str) -> str: ...
    def get_file_hashes(self) -> Iterable[str]: ...
    def get_object_source(self, instance: object) -> Optional[str]: ...
    def get_types(self) -> Iterable[Tuple[str, List[SourceInfo]]]: ...
    def register_code(self, type_name: str, instance: object) -> None: ...

class SourceInfo(object):
    __doc__: str
    _content: None
    _hash: None
    _requires: None
    content: str
    hash: str
    module_name: str
    path: str
    requires: List[str]
    def __init__(self, path: str, module_name: str) -> None: ...
    def _get_module_name(self) -> str: ...

class SourceNotFoundException(Exception):
    __doc__: str
