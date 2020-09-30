# (generated with --quick)

import flask.app
import flask.wrappers
from typing import Any, List, Optional, Type

AbstractTransport: Any
Flask: Type[flask.app.Flask]
Resource: Any
Router: Any
json: module
request: flask.wrappers.Request
requests: module

class Facebook(Any):
    ENDPOINTS_TO_ADD: List[str]
    MESSAGES_URL: str
    access_point_root: Optional[str]
    access_token: str
    router: Any
    verify_token: Optional[str]
    def __init__(self, router, access_token: str, verify_token: str, access_point_root: str) -> None: ...
    def get_end_points_to_add(self) -> List[str]: ...
    def send_message(self, recipient_id: int, message_text: str) -> None: ...

class FacebookEndPoint(Any):
    app: Optional[flask.app.Flask]
    fb: Optional[Facebook]
    methods: List[str]
    def __init__(self, transport: Facebook, app: flask.app.Flask) -> None: ...
    def get(self) -> Any: ...
    def get_privacy(self) -> None: ...
    def post(self) -> tuple: ...
    def verify(self) -> tuple: ...
    def webhook(self, data) -> tuple: ...
