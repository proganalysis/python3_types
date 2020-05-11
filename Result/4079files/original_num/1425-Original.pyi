# (generated with --quick)

import redis.client
import sqlite3.dbapi2
import src.objects.user
from typing import Any, Type

User: Type[src.objects.user.User]
answer: str
c: sqlite3.dbapi2.Cursor
config: Any
conn: sqlite3.dbapi2.Connection
r: redis.client.Redis
redis: module
sqlite3: module

class FakeUser:
    id: Any
    username: None
    def __init__(self, user_id) -> None: ...

def migrate() -> None: ...
def reset_local_redis_database() -> None: ...
