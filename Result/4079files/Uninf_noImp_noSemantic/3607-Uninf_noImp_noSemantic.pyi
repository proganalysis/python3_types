from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import ModelSchema, ModelSchemaOpts
from typing import Any

class FlaskMarshmallowFactory(Marshmallow):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class BaseOpts(ModelSchemaOpts):
    def __init__(self, meta: Any) -> None: ...

class BaseSchema(ModelSchema):
    OPTIONS_CLASS: Any = ...

ma: Any
