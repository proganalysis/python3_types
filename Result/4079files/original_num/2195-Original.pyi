# (generated with --quick)

from typing import Any, List, Tuple, Type

Path: Type[pathlib.Path]
numpy: module
pathlib: module

def load_ply(filename, enableCaching = ...) -> Tuple[Any, Any, Any]: ...
def load_ply_just_xyz(plyFilePath, enableCaching = ...) -> Any: ...
def load_ply_using_library(filename) -> Tuple[Any, list, List[str]]: ...
def save_ply(xyz, filename) -> None: ...