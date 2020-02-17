# (generated with --quick)

from typing import Any, Type

Marshmallow: Any
ModelSchema: Any
ModelSchemaOpts: Any
db: Any
ma: FlaskMarshmallowFactory

class BaseOpts(Any):
    def __init__(self, meta) -> None: ...

class BaseSchema(Any):
    OPTIONS_CLASS: Type[BaseOpts]

class FlaskMarshmallowFactory(Any):
    def __init__(self, *args, **kwargs) -> None: ...
