# (generated with --quick)

from typing import Any

ReprBuilder: Any
db: Any
generate_uuid: Any

class Subject(Any):
    __doc__: str
    __tablename__: str
    id: Any
    name: Any
    title: Any
    type_: Any
    def __init__(self, name: str, title: str, type_: str) -> None: ...
    def __repr__(self) -> str: ...
