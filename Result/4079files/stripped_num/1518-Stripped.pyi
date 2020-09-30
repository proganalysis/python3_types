# (generated with --quick)

import flask.sessions
from typing import Any, Tuple, Type
import uuid
import werkzeug.datastructures

CallbackDict: Type[werkzeug.datastructures.CallbackDict]
MongoClient: Any
SessionInterface: Type[flask.sessions.SessionInterface]
SessionMixin: Type[flask.sessions.SessionMixin]
__author__: str
__copyright__: str
__license__: str
__version__: str
__version_info__: Tuple[str, str, str]
datetime: Type[datetime.datetime]
pymongo: Any

class MongoSession(werkzeug.datastructures.CallbackDict, flask.sessions.SessionMixin):
    manager: Any
    modified: bool
    permanent: Any
    session_id: Any
    user_id: Any
    def __init__(self, data = ..., session_id = ..., user_id = ..., permanent = ..., manager = ...) -> None: ...
    def is_authenticated(self) -> bool: ...
    def login(self, uid) -> None: ...
    def logout(self) -> None: ...
    def logout_all_devices(self) -> None: ...

class MongoSessionInterface(flask.sessions.SessionInterface):
    _manager: MongoSessionManager
    collection_name: str
    def __init__(self, *args, **kwargs) -> None: ...
    def open_session(self, app, request) -> MongoSession: ...

class MongoSessionManager:
    _client: Any
    _collection: Any
    _db: Any
    _permanent: Any
    collection_name: str
    def __init__(self, db = ..., permanent = ..., *args, **kwargs) -> None: ...
    def _check_indexes(self) -> None: ...
    def get_session(self, sid) -> MongoSession: ...
    def logout_all_devices(self, session) -> None: ...
    def update_session(self, session, expired) -> None: ...

def uuid4() -> uuid.UUID: ...
