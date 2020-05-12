# (generated with --quick)

from typing import Any, Type, TypeVar

BigInteger: Any
Column: Any
DateTime: Any
IDType: Any
ItemType: Any
Session: Any
String: Any
sessionmaker: Any
sqlfunc: Any
uuid: module

_T0 = TypeVar('_T0')
_TAutoCloseSession = TypeVar('_TAutoCloseSession', bound=AutoCloseSession)

class AutoCloseSession(Any):
    def __enter__(self: _TAutoCloseSession) -> _TAutoCloseSession: ...
    def __exit__(self, type, value, traceback) -> None: ...

class AutoCloseSessionMaker(Any):
    class_: Type[AutoCloseSession]
    def __call__(self, **local_kw) -> Any: ...
    def __init__(self, **kw) -> None: ...

class CreatedAtMixin(object):
    created_at: Any

class DictableMixin(object):
    def to_dict(self) -> dict: ...

class IntegerPrimaryKeyMixin(object):
    id: Any

class SQLAlchemyMixin(object):
    model: None
    def delete_item(self, item_id, session) -> bool: ...
    def get_item(self, item_id, session) -> Any: ...
    def get_table(self, session) -> Any: ...
    def list_items(self, n_items = ..., session = ...) -> Any: ...
    def post_item(self, item, session) -> Any: ...
    def put_item(self, item_id: _T0, item, session) -> _T0: ...
    def update_item(self, item_id, partial_body, session) -> bool: ...

class StringPrimaryKeyMixin(object):
    id: Any

class UpdatedAtMixin(object):
    updated_at: Any

def _uuid() -> str: ...
