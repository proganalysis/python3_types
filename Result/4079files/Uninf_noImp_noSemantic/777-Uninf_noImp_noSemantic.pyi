from buck_tool import BuckTool
from typing import Any

SERVER: Any
BOOTSTRAPPER: Any
BUCKFILESYSTEM: Any
BUCK_BINARY_HASH: Any
PEX_ONLY_EXPORTED_RESOURCES: Any
MODULES_DIR: str
MODULES_RESOURCES_DIR: str

class BuckPackage(BuckTool):
    _resource_subdir: Any = ...
    _lock_file: Any = ...
    def __init__(self, buck_project: Any, buck_reporter: Any) -> None: ...
    def _get_package_info(self): ...
    def _get_buck_git_commit(self): ...
    def _get_resource_dir(self): ...
    def _get_resource_subdir(self): ...
    def __create_dir(self, dir: Any) -> None: ...
    def _get_resource_lock_path(self): ...
    def _has_resource(self, resource: Any): ...
    def _get_resource(self, resource: Any): ...
    def _unpack_resource(self, resource_path: Any, resource_name: Any, resource_executable: Any) -> None: ...
    def _get_extra_java_args(self): ...
    def _get_exported_resources(self): ...
    def _get_bootstrap_classpath(self): ...
    def _get_buckfilesystem_classpath(self): ...
    def _get_java_classpath(self): ...
    def _get_buck_binary_hash(self): ...
    def _unpack_modules(self) -> None: ...
    def _unpack_dir(self, resource_dir: Any, dst_dir: Any) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
