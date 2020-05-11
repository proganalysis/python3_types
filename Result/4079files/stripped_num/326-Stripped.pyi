# (generated with --quick)

import flask.wrappers
from typing import Any, Callable, NoReturn, Sequence, Tuple, Union
import werkzeug.wrappers

AuthID: Any
Authable: Any
Authorised: Any
BadRequest: Any
Env: Any
Password: Any
Priv: Any
Token: Any
TokenID: Any
User: Any
UserID: Any
Username: Any
request: flask.wrappers.Request

class Auth(Any):
    def authoriseRequest(self, req, priv) -> Tuple[Any, Any]: ...
    def authoriseRoute(self, priv) -> Callable[[Any], Any]: ...
    def authoriseTokenId(self, tokenId, priv) -> Tuple[Any, Any]: ...
    def authoriseUser(self, username, password, priv) -> Tuple[Any, Any]: ...
    def loginUser(self, username, password) -> Tuple[Any, Any]: ...
    def registerUser(self, name, password, privs = ...) -> Any: ...

def __getattr__(name) -> Any: ...
def abort(status: Union[int, werkzeug.wrappers.Response], *args, **kwargs) -> NoReturn: ...
def wraps(wrapped: Callable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable[[Callable], Callable]: ...
