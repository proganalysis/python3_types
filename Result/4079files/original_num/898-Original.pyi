# (generated with --quick)

from typing import Any

DAY_IN_SECONDS: int
HttpResponseForbidden: Any
JsonResponse: Any
TOKEN_DURATION: float
VariantsDb: Any
auth: Any
authenticate: Any
deactivate_if_not_found_on_disk: Any
json_view: Any
logger: logging.Logger
logging: module
renew_token: Any
secret: Any
settings: Any
update_if_db_changed: Any
user_factory: Any

class protected:
    __doc__: str
    level: Any
    def __call__(self, request, **kwargs) -> Any: ...
    def __init__(self, view, level = ...) -> None: ...
    def view(self) -> Any: ...

def JWT_user(user, duration = ...) -> Any: ...
