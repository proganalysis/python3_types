"""Where HTTP errors (responses) are defined."""

from webargs.flaskparser import (use_args, parser)
from werkzeug.exceptions import HTTPException
import flask_restful

from . import utils

ERRORS = {
    'BadRequest': utils.load_json_mock('error_400'),
    'NotFound': utils.load_json_mock('error_404'),
    'MethodNotAllowed': utils.load_json_mock('error_405'),
    'TooManyRequests': utils.load_json_mock('error_429'),
    'InternalServerError': utils.load_json_mock('error_500'),
    'PaymentRequired': utils.load_json_mock('error_402'),
    # FIXME: needs 403 unauthorized (valid user, but no access)
}
"""dict: Key name is the werkzeug error and the value is the
JSON mock to use as the response.

The mocks are the base of the error response, which may have
more context added in certain responses.
"""


class PaymentRequired(HTTPException):
    """Free users prohibited."""
    code = 402
    description = 'Payment required.'


@parser.error_handler
def handle_arg_schema_error(error):
    """RESTful error regarding webarg schema mismatch (invalidation).

    Arguments:
        error (???): An error object from webargs, passed to this
        function when a request's arguments are not valid according to
        the specified webargs schema (a dict, see: use_args decorator).

    Returns:
        json "error"...

    """

    flask_restful.abort(400, validationError=error.messages)
