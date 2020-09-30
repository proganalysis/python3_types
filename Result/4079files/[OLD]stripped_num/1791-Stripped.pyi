# (generated with --quick)

from typing import Any, Counter, Dict, Tuple, TypeVar, Union

GenerationFailedException: Any
StringGenerator: Any
collections: module
os: module
weighted_choice: Any

_T1 = TypeVar('_T1')

class FilePathGenerator:
    BUILD_FILE_NAME: str
    _available_directories: Dict[Tuple[Any, Any], Tuple[Any, Any, Any]]
    _build_file_sizes: Counter[nothing]
    _component_generator: Any
    _file_depths_in_package: Counter[nothing]
    _file_samples: collections.defaultdict
    _file_samples_dirty: bool
    _last_package_path: Any
    _last_package_remaining_targets: Any
    _package_depths: Counter[nothing]
    _package_paths: Dict[nothing, nothing]
    _root: Dict[Any, Dict[nothing, nothing]]
    _sizes_by_depth: collections.defaultdict[int, Any]
    _sizes_by_depth_in_package: collections.defaultdict[int, Any]
    def __init__(self) -> None: ...
    def _generate_name(self, directory, generator, extension = ...) -> Any: ...
    def _generate_parent(self, package_key, root: _T1, depth, sizes_by_depth, component_generator) -> Tuple[Any, Union[Dict[nothing, nothing], _T1]]: ...
    def _generate_path(self, package_key, root, depth, sizes_by_depth, component_generator, extension = ...) -> Tuple[Any, Any]: ...
    def _split_path_into_components(self, path) -> list: ...
    def add_package_file_sample(self, package_path, relative_path) -> None: ...
    def analyze_project_data(self, project_data) -> None: ...
    def generate_package_path(self) -> Any: ...
    def generate_path_in_package(self, package_path, depth, component_generator, extension) -> Any: ...
    def register_path(self, path) -> None: ...
