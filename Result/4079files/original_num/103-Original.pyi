# (generated with --quick)

import flask.wrappers
from typing import Any, Optional

build: Any
client: Any
httplib2: module
request: flask.wrappers.Request
service: Any
session: Any
url_for: Any

def get_google_auth_flow(login: Optional[str] = ...) -> Any: ...
def get_google_authorize_uri(flow) -> str: ...
def get_google_person(flow) -> Any: ...
