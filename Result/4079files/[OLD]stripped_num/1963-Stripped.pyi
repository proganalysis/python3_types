# (generated with --quick)

import abc
from typing import Any, Type

ABCMeta: Type[abc.ABCMeta]
ClassProperty: Any
HTTPModelManager: Any

class HTTPModel(metaclass=abc.ABCMeta):
    HTTPMeta: type
    _HTTPModel__manager: None
    objects: Any
    def _HTTPModel__get_pk(self) -> Any: ...
    def delete(self) -> Any: ...
