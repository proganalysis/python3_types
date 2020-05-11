# (generated with --quick)

from typing import Any, Dict

Column: Any
Date: Any
ForeignKey: Any
Integer: Any
Time: Any
datetime: module
db: Any
exc: Any

class Item(Any):
    __tablename__: str
    id: Any
    reservations: Any
    def __getstate__(self) -> Dict[str, Any]: ...

class Reservation(Any):
    __tablename__: str
    date: Any
    duration: Any
    id: Any
    item_id: Any
    start_time: Any
    def __getstate__(self) -> Dict[str, Any]: ...
    def update_from_json(self, **kwargs) -> None: ...
