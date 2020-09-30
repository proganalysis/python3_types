# (generated with --quick)

from typing import Any, Tuple, TypeVar, Union

base: module
swagger_client: Any
sys: module

_T0 = TypeVar('_T0')

class Label(base.Base):
    def add_label_to_image(self, label_id, repository, tag, **kwargs) -> Any: ...
    def create_label(self, name: _T0 = ..., desc = ..., color = ..., scope = ..., project_id = ..., **kwargs) -> Tuple[Any, Union[str, _T0]]: ...
    def delete_label(self, label_id, **kwargs) -> Any: ...
