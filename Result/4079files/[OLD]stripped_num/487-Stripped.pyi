# (generated with --quick)

import functools
import jinja2.environment
import jinja2.loaders
from typing import Any, Callable, Dict, Sequence, Type

Base: Any
Column: Any
DATABASE_URI: str
Environment: Type[jinja2.environment.Environment]
Integer: Any
Klein: Any
PackageLoader: Type[jinja2.loaders.PackageLoader]
Session: Any
String: Any
Unicode: Any
app: Any
create_engine: Any
db: Any
db_engine: Any
db_session: Any
declarative_base: Any
env: jinja2.environment.Environment
fortune: Any
json: module
jsonHandler: Any
os: module
partial: Type[functools.partial]
plaintext: Any
queries: Any
route: Any
run: Any
sessionmaker: Any
sys: module
updates: Any
xrange: Type[range]

class Fortune(Any):
    __tablename__: str
    id: Any
    message: Any
    def serialize(self) -> Dict[str, Any]: ...

class World(Any):
    __tablename__: str
    id: Any
    randomNumber: Any
    def serialize(self) -> Dict[str, Any]: ...

def attrgetter(*attrs: str) -> Callable[[Any], tuple]: ...
def close_session(func) -> Callable: ...
def getQueryNum(queryString) -> int: ...
def randint(a: int, b: int) -> int: ...
def wraps(wrapped: Callable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable[[Callable], Callable]: ...
