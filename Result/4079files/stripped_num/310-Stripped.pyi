# (generated with --quick)

import flask.app
import flask.wrappers
from typing import Any, List, Type

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
    access_point_root: Any
    access_token: Any
    router: Any
    verify_token: Any
    def __init__(self, router, access_token, verify_token, access_point_root) -> None: ...
    def get_end_points_to_add(self) -> List[str]: ...
    def send_message(self, recipient_id, message_text) -> None: ...

class FacebookEndPoint(Any):
    app: Any
    fb: Any
    methods: List[str]
    def __init__(self, transport, app) -> None: ...
    def get(self) -> Any: ...
    def get_privacy(self) -> None: ...
    def post(self) -> Any: ...
    def verify(self) -> Any: ...
    def webhook(self, data) -> Any: ...
