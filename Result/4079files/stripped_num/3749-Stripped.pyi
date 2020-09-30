# (generated with --quick)

import pymysql.connections
from typing import Any, Dict, Optional, TextIO, Union

db_db: str
db_host: str
db_password: str
db_port: int
db_user: str
json: module
json_file: str
mysql: Any
outfile: TextIO
pymysql: module
ret: Dict[str, Any]
t0: float
time: module

class Database(object):
    db: pymysql.connections.Connection
    def __init__(self, host, port, user, password, db) -> None: ...
    def `exec`(self, sql, args = ..., r_dict = ..., fetch_all = ..., ret_row = ...) -> Optional[Union[tuple, Dict[str, Any]]]: ...
