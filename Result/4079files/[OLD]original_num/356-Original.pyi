# (generated with --quick)

from typing import Any, Optional

FakeDate: Any
FakeDatetime: Any
FrozenDateTimeFactory: Any
Models: Any
_connections: dict
bot: Any
convert_to_timezone_naive: Any
databot: Any
datetime: module
dateutil: module
db: Any
freezetime: Any
io: module
os: module
pathlib: module
pytest: Any
requests: Any
requests_mock: Any
sa: Any
sqlalchemy: Any
sqlite: Any

class Db:
    engine: Any
    meta: Any
    models: Any
    uri: Any
    def Bot(self) -> Any: ...
    def __init__(self) -> None: ...
    def finalize(self) -> None: ...

class MySqlDb(Db):
    engine: Any
    meta: Any
    models: Any
    name: str
    uri: Optional[str]
    def get_connection_uri(self) -> Optional[str]: ...

class NoDatabaseFixture(object):
    error: Any
    def __init__(self, error) -> None: ...

class PostgreSqlDb(Db):
    engine: Any
    meta: Any
    models: Any
    name: str
    uri: str
    def get_connection_uri(self) -> str: ...

class SqliteDb(Db):
    engine: Any
    meta: Any
    models: Any
    name: str
    uri: Any
    def get_connection_uri(self) -> str: ...

def get_db_connection(name, uri) -> Any: ...
