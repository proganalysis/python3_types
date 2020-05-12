# (generated with --quick)

import pathlib
from typing import Any, Generator, List, Type

Nifti1Pair: Any
Path: Type[pathlib.Path]
SingleConditionSpec: Any
SpatialImage: Any
__all__: List[str]
logger: logging.Logger
logging: module
nib: Any
np: module

def load_boolean_mask(path, predicate = ...) -> Any: ...
def load_images(image_paths) -> Generator[Any, Any, None]: ...
def load_images_from_dir(in_dir, suffix = ...) -> Generator[Any, Any, None]: ...
def load_labels(path) -> list: ...
def save_as_nifti_file(data, affine, path) -> None: ...
