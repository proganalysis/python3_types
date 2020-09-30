# (generated with --quick)

import abc
from typing import Any, Callable, Dict, Type, TypeVar, Union

ABC: Type[abc.ABC]
Reshape: Any
Sequential: Any
get_images_matrix: Any
lines: Any
scipy: Any

_FuncT = TypeVar('_FuncT', bound=Callable)

class AImageModel(abc.ABC):
    __doc__: str
    @abstractmethod
    def model(self) -> Any: ...
    def process_input(self, image_batch) -> None: ...

class VGGImageModel(AImageModel):
    __doc__: str
    _id_map: Dict[Any, int]
    _model: Any
    _vgg_features: Any
    def __init__(self, data_root) -> None: ...
    def model(self) -> Any: ...
    def process_input(self, image_batch) -> Any: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
@overload
def pjoin(path: Union[bytes, _PathLike[bytes]], *paths: Union[bytes, _PathLike[bytes]]) -> bytes: ...
@overload
def pjoin(path: Union[str, _PathLike[str]], *paths: Union[str, _PathLike[str]]) -> str: ...
