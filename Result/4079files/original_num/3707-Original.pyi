# (generated with --quick)

import abc
import flask.wrappers
from typing import Any, Callable, Dict, List, NoReturn, Tuple, Type, TypeVar

ABC: Type[abc.ABC]
CustomException: Any
IntegrityError: Any
OperationalError: Any
RequestNotAllowed: Any
ResourceNotFound: Any
SQLIntegrityError: Any
SQlOperationalError: Any
db: Any
request: flask.wrappers.Request

_FuncT = TypeVar('_FuncT', bound=Callable)

class AssociationModelResource(abc.ABC):
    auth_required: bool
    default_limit: int
    exclude: Tuple[str]
    exclude_related_resource: Tuple[str]
    filters: Dict[nothing, nothing]
    include: Tuple[str]
    limit: int
    max_limit: int
    model: None
    obj_exclude: Any
    obj_only: tuple
    obj_optional: List[str]
    only: Tuple[str]
    optional: Tuple[str]
    order_by: List[str]
    page: int
    roles_accepted: Tuple[str]
    roles_required: Tuple[str]
    schema: None
    def add_relation(self, data) -> None: ...
    def apply_filters(self, queryset, **kwargs) -> Any: ...
    def apply_ordering(self, queryset, order_by) -> Any: ...
    @abstractmethod
    def has_add_permission(self, obj, data) -> bool: ...
    @abstractmethod
    def has_change_permission(self, obj, data) -> bool: ...
    @abstractmethod
    def has_delete_permission(self, obj, data) -> bool: ...
    @abstractmethod
    def has_read_permission(self, qs) -> Any: ...
    def remove_relation(self, data) -> None: ...
    def update_relation(self, data) -> NoReturn: ...

class ModelResource(abc.ABC):
    auth_required: bool
    default_limit: int
    exclude: Tuple[str]
    exclude_related_resource: Tuple[str]
    export: bool
    filters: Dict[nothing, nothing]
    include: Tuple[str]
    limit: int
    max_export_limit: int
    max_limit: int
    model: None
    obj_exclude: Any
    obj_only: tuple
    obj_optional: List[str]
    only: Tuple[str]
    optional: Tuple[str]
    order_by: List[str]
    page: int
    roles_accepted: Tuple[str]
    roles_required: Tuple[str]
    schema: None
    def apply_filters(self, queryset, **kwargs) -> Any: ...
    def apply_ordering(self, queryset, order_by) -> Any: ...
    @abstractmethod
    def has_add_permission(self, obj) -> bool: ...
    @abstractmethod
    def has_change_permission(self, obj) -> bool: ...
    @abstractmethod
    def has_delete_permission(self, obj) -> bool: ...
    @abstractmethod
    def has_read_permission(self, qs) -> Any: ...
    def patch_resource(self, obj) -> Tuple[Dict[str, Any], int]: ...
    def save_resource(self) -> Tuple[Dict[str, Any], int]: ...
    def update_resource(self) -> Tuple[Dict[str, Any], int]: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
