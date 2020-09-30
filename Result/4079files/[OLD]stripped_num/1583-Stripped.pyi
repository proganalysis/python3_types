# (generated with --quick)

from typing import Dict, NoReturn, Type, Union

ERRORS: Dict[int, Type[Union[MethodNotAllowed, Unauthorized]]]

class AxisException(Exception):
    __doc__: str

class LoginRequired(AxisException):
    __doc__: str

class MethodNotAllowed(AxisException):
    __doc__: str

class NoPermission(AxisException):
    __doc__: str

class RequestError(AxisException):
    __doc__: str

class ResponseError(AxisException):
    __doc__: str

class Unauthorized(AxisException):
    __doc__: str

def raise_error(error) -> NoReturn: ...
