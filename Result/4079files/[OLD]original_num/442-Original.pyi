# (generated with --quick)

import json.encoder
from typing import Any, Callable, Optional, Tuple, Type, Union

EmptyPage: Any
HashAuthView: Any
Http404: Any
HttpResponse: Any
HttpResponseForbidden: Any
HttpResponseRedirect: Any
InvalidPage: Any
ListView: Any
View: Any
_: Any
method_decorator: Any
settings: Any

class AllowedSubnetMixin(object):
    def dispatch(self, request, *args, **kwargs) -> Any: ...

class AuthenticatedOrHashAuthView(Any):
    def dispatch(self, request, *args, **kwargs) -> Any: ...

class BaseListWithFiltering(RedirectWhenErrorMixin, Any):
    __doc__: str
    def paginate_queryset(self, queryset, page_size) -> Tuple[Any, Any, Any, Any]: ...

class OrderedFilteredList(OrderingMixin, BaseListWithFiltering):
    paginate_by: Any

class OrderingMixin(object):
    __doc__: str
    def get_context_data(self, **kwargs) -> Any: ...
    def get_ordering(self) -> Optional[str]: ...

class RedirectWhenError(Exception):
    message: Any
    url: Any
    def __init__(self, url, failed_message = ...) -> None: ...
    def __str__(self) -> Any: ...

class RedirectWhenErrorMixin(object):
    def get(self, request, *args, **kwargs) -> Any: ...

class SecureApiView(AllowedSubnetMixin, Any): ...

def dumps(obj, skipkeys: bool = ..., ensure_ascii: bool = ..., check_circular: bool = ..., allow_nan: bool = ..., cls: Optional[Type[json.encoder.JSONEncoder]] = ..., indent: Optional[Union[int, str]] = ..., separators: Optional[Tuple[str, str]] = ..., default: Optional[Callable[[Any], Any]] = ..., sort_keys: bool = ..., **kwds) -> str: ...
def hash_auth_view(fn) -> Callable: ...
def ip_address(address: object) -> Any: ...
def ip_network(address: object, strict: bool = ...) -> Any: ...
