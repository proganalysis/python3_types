# (generated with --quick)

from typing import Any, Dict, Tuple, Type

BotTimeout = TimedOutError

base_errors: Dict[int, type]

class AuthKeyError(RPCError):
    __doc__: str
    code: Any
    message: Any

class BadRequestError(RPCError):
    __doc__: str
    code: Any
    message: Any

class FloodError(RPCError):
    __doc__: str
    code: Any
    message: Any

class ForbiddenError(RPCError):
    __doc__: str
    code: Any
    message: Any

class InvalidDCError(RPCError):
    __doc__: str
    code: Any
    message: Any

class NotFoundError(RPCError):
    __doc__: str
    code: Any
    message: Any

class RPCError(Exception):
    __doc__: str
    code: Any
    message: Any
    def __init__(self, request, message, code = ...) -> None: ...
    def __reduce__(self) -> Tuple[Type[RPCError], Tuple[Any, Any]]: ...
    @staticmethod
    def _fmt_request(request) -> str: ...

class ServerError(RPCError):
    __doc__: str
    code: Any
    message: Any

class TimedOutError(RPCError):
    __doc__: str
    code: Any
    message: Any

class UnauthorizedError(RPCError):
    __doc__: str
    code: Any
    message: Any
