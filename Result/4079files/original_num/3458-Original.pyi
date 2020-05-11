# (generated with --quick)

from typing import Any, Dict, Type, TypeVar
import uuid

Base: Any
Boolean: Any
Column: Any
DB_CONNECTION_STRING: str
Date: Any
ForeignKey: Any
Integer: Any
Session: Any
String: Any
Text: Any
api_key_authentication: Any
config: Any
create_engine: Any
datetime: Type[datetime.datetime]
declarative_base: Any
engine: Any
hug: Any
json: module
logging: module
pg_host: Any
pg_pass: Any
pg_user: Any
relationship: Any
session: Any
sessionmaker: Any

_T0 = TypeVar('_T0')

class KlaxerMessage(Any):
    __doc__: str
    __tablename__: str
    can_dismiss: Any
    id: Any
    text: Any
    user_id: Any
    def __repr__(self) -> str: ...

class KlaxerUser(Any):
    __doc__: str
    __tablename__: str
    api_key: Any
    approved: Any
    calls: Any
    email: Any
    id: Any
    messages: Any
    name: Any
    registered: Any
    signup_date: Any
    def __repr__(self) -> str: ...
    def to_dict(self) -> Dict[str, Any]: ...
    def to_json(self, *args, **kwargs) -> str: ...

def add_message(user, text, can_dismiss = ...) -> KlaxerMessage: ...
def approve(user: _T0) -> _T0: ...
def bootstrap() -> None: ...
def create_user(name, email) -> KlaxerUser: ...
def is_existing_user(email) -> bool: ...
def register(name, email) -> KlaxerUser: ...
def uuid4() -> uuid.UUID: ...
def verify(api_key) -> Any: ...
