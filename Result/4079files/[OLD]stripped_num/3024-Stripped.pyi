# (generated with --quick)

from typing import Any

AutoCloseSessionMaker: Any
Engine: Any
IntegrityError: Any
JSONType: Any
Request: Any
Response: Any
SQLAlchemyMixin: Any
SQLItemResource: Any
SQLRootResource: Any
create_engine: Any
falcon: Any
hooks: Any

class _SQLResource(Any):
    _engine: Any
    _session_maker: Any
    _sqlurl: Any
    schema: None
    def __init__(self, sqlurl_or_engine, **kwargs) -> None: ...
    def make_session(self, **kwds) -> Any: ...
    def set_engine(self, engine, **kwargs) -> None: ...

def put_json_to_context(res, item, key = ...) -> None: ...
