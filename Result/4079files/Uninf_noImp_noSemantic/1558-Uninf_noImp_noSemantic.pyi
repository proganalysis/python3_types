from typing import Any
from webargs.flaskparser import use_args as use_args
from werkzeug.exceptions import HTTPException

ERRORS: Any

class PaymentRequired(HTTPException):
    code: int = ...
    description: str = ...

def handle_arg_schema_error(error: Any) -> None: ...
