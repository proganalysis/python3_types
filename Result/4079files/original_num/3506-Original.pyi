# (generated with --quick)

import flask.app
import flask.wrappers
import flask_injector
from typing import Any, Type

Base: Any
Column: Any
Flask: Type[flask.app.Flask]
FlaskInjector: Type[flask_injector.FlaskInjector]
Injector: Any
Module: Any
NoResultFound: Any
Request: Type[flask.wrappers.Request]
SQLAlchemy: Any
String: Any
declarative_base: Any
il: logging.Logger
inject: Any
logging: module
singleton: Any

class AppModule(Any):
    app: Any
    def __init__(self, app) -> None: ...
    def configure(self, binder) -> None: ...
    def configure_db(self, app) -> Any: ...

class KeyValue(Any):
    __tablename__: str
    key: Any
    value: Any
    def __init__(self, key, value) -> None: ...
    def serializable(self) -> None: ...

def configure_views(app) -> None: ...
def jsonify(*args, **kwargs) -> Any: ...
def main() -> None: ...
