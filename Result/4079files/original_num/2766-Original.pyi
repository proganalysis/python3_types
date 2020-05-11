# (generated with --quick)

from typing import Any, Type, TypeVar
import werkzeug.wrappers

Admin: Any
AdminIndexView: Any
admin: Any
current_user: Any
expose: Any

_RC = TypeVar('_RC', bound=werkzeug.wrappers.Response)

class MyAdminIndexView(Any):
    index: Any
    def __init__(self, endpoint = ..., url = ...) -> None: ...

@overload
def redirect(location, code: int = ..., Response: None = ...) -> werkzeug.wrappers.Response: ...
@overload
def redirect(location, code: int = ..., Response: Type[_RC] = ...) -> _RC: ...
def url_for(endpoint, **values) -> Any: ...
