from .types import IDType, ItemType
from sqlalchemy.orm import Session, sessionmaker
from typing import Any, List, Optional

def _uuid(): ...

class AutoCloseSession(Session):
    def __enter__(self): ...
    def __exit__(self, type: Any, value: Any, traceback: Any) -> None: ...

class AutoCloseSessionMaker(sessionmaker):
    class_: Any = ...
    def __init__(self, **kw: Any) -> None: ...
    def __call__(self, **local_kw: Any) -> AutoCloseSession: ...

class IntegerPrimaryKeyMixin:
    id: Any = ...

class StringPrimaryKeyMixin:
    id: Any = ...

class CreatedAtMixin:
    created_at: Any = ...

class UpdatedAtMixin:
    updated_at: Any = ...

class DictableMixin:
    def to_dict(self): ...

class SQLAlchemyMixin:
    model: Any = ...
    def __init__(self) -> None: ...
    def get_table(self, session: Session) -> Any: ...
    def list_items(self, n_items: Any=..., session: Session=...) -> List[DictableMixin]: ...
    def get_item(self, item_id: IDType, session: Session) -> Optional[DictableMixin]: ...
    def post_item(self, item: ItemType, session: Session) -> IDType: ...
    def put_item(self, item_id: IDType, item: ItemType, session: Session) -> IDType: ...
    def update_item(self, item_id: IDType, partial_body: ItemType, session: Session) -> bool: ...
    def delete_item(self, item_id: IDType, session: Session) -> bool: ...