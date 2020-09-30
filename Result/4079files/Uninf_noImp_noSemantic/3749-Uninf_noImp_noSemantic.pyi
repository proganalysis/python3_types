from typing import Any

db_host: str
db_port: int
db_user: str
db_password: str
db_db: str
json_file: str

class Database:
    db: Any = ...
    def __init__(self, host: Any, port: Any, user: Any, password: Any, db: Any) -> None: ...
    def exec(self, sql: str, args: Any=..., r_dict: bool=..., fetch_all: bool=..., ret_row: bool=...) -> Any: ...

t0: Any
ret: Any
