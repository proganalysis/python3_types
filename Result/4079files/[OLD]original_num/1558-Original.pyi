# (generated with --quick)

from typing import Any, Dict, Type
import werkzeug.exceptions

ERRORS: Dict[str, Any]
HTTPException: Type[werkzeug.exceptions.HTTPException]
flask_restful: Any
handle_arg_schema_error: Any
parser: Any
use_args: Any
utils: Any

class PaymentRequired(werkzeug.exceptions.HTTPException):
    __doc__: str
    code: int
    description: str
