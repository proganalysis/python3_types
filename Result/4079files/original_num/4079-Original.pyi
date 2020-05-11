# (generated with --quick)

import numpy
import pathlib
from typing import Any, Callable, Iterable, List, Optional, Type, Union

Nifti1Pair: Any
Path: Type[pathlib.Path]
SingleConditionSpec: Any
SpatialImage: Any
__all__: List[str]
logger: logging.Logger
logging: module
nib: Any
np: module

def load_boolean_mask(path: Union[str, pathlib.Path], predicate: Optional[Callable[[numpy.ndarray], numpy.ndarray]] = ...) -> numpy.ndarray: ...
def load_images(image_paths: Iterable[Union[str, pathlib.Path]]) -> Iterable: ...
def load_images_from_dir(in_dir: Union[str, pathlib.Path], suffix: str = ...) -> Iterable: ...
def load_labels(path: Union[str, pathlib.Path]) -> list: ...
def save_as_nifti_file(data: numpy.ndarray, affine: numpy.ndarray, path: Union[str, pathlib.Path]) -> None: ...
