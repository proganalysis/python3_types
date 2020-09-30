# (generated with --quick)

import flask.wrappers
from typing import Any, List, Type, TypeVar
import werkzeug.wrappers

AUTHORIZATION_URI: str
Namespace: Any
OAuth2Session: Any
Resource: Any
SCOPE: List[str]
TOKEN_URI: str
TokenType: Any
USER_PROFILE_URI: str
client_id: str
client_secret: str
get_jwt_token: Any
get_token_redirect_response: Any
json: module
os: module
redirect_uri: str
request: flask.wrappers.Request
session: Any

_RC = TypeVar('_RC', bound=werkzeug.wrappers.Response)

def get_user_info(google_session) -> Any: ...
@overload
def redirect(location, code: int = ..., Response: None = ...) -> werkzeug.wrappers.Response: ...
@overload
def redirect(location, code: int = ..., Response: Type[_RC] = ...) -> _RC: ...
def register_google_oauth(namespace) -> None: ...
