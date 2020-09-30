# (generated with --quick)

import inet
import ssl
import typing
from typing import Callable, Dict, List, Mapping, Sequence, Tuple, Type, TypeVar, Union
import urllib.request

All: typing.Any
Any: typing.Any
Client: Type[inet.Client]
HTTPError: typing.Any
Optional: typing.Any
Range: typing.Any
Request: Type[urllib.request.Request]
Required: typing.Any
__version__: typing.Any
json: module
parseString: typing.Any
port_def: typing.Any
pprint: module
socket: module
time: module

AnyStr = TypeVar('AnyStr', str, bytes)

class HTTPClient(inet.Client):
    NO_CONTENT: typing.Any
    __doc__: str
    attr_name: str
    default_headers: typing.Any
    extra_headers: typing.Any
    host: typing.Any
    port: typing.Any
    response: typing.Optional[HTTPResponse]
    serializers: Dict[str, Union[Type[str], Callable[..., str]]]
    timeout: typing.Any
    tries: typing.Any
    user_agent: Tuple[str, str]
    wait: typing.Any
    def __init__(self, host: typing.Any, port: typing.Any, timeout: typing.Any, tries: typing.Any, wait: typing.Any, headers: typing.Any, extra_headers: typing.Any = ...) -> None: ...
    def _get_serializer(self, headers: typing.Any) -> Union[Type[str], Callable[..., str]]: ...
    def close(self) -> None: ...
    def delete(self, *args, **kwargs) -> None: ...
    def get(self, *args, **kwargs) -> None: ...
    def patch(self, *args, **kwargs) -> None: ...
    def post(self, *args, **kwargs) -> None: ...
    def put(self, *args, **kwargs) -> None: ...
    def request(self, method: typing.Any, path: typing.Any, headers: typing.Any = ..., timeout: typing.Any = ..., data: typing.Any = ...) -> None: ...
    @staticmethod
    def validator() -> dict: ...

class HTTPResponse:
    __doc__: str
    content: typing.Any
    deserializers: Dict[str, typing.Any]
    headers: typing.Any
    reason: typing.Any
    response_provided: bool
    status_code: typing.Any
    version: typing.Any
    def __getattribute__(self, name: typing.Any) -> typing.Any: ...
    def __init__(self, response: typing.Any = ...) -> None: ...
    def _formated_content(self) -> str: ...
    def _get_content(self, response: typing.Any) -> typing.Any: ...
    def assert_header_has(self, header: typing.Any, expected_value: typing.Any, separator: typing.Any = ...) -> None: ...
    def assert_header_is(self, header: typing.Any, expected_values: typing.Any, separator: typing.Any = ...) -> None: ...
    def assert_reason(self, reason: typing.Any) -> None: ...
    def assert_status_code(self, status_code: typing.Any) -> None: ...

class NoResponseProvidedError(Exception):
    __doc__: str

def parse_qsl(qs: typing.Optional[AnyStr], keep_blank_values: bool = ..., strict_parsing: bool = ..., encoding: str = ..., errors: str = ...) -> List[Tuple[AnyStr, AnyStr]]: ...
def urlencode(query: Union[Mapping, Sequence[Tuple[typing.Any, typing.Any]]], doseq: bool = ..., safe: AnyStr = ..., encoding: str = ..., errors: str = ..., quote_via: Callable[[str, AnyStr, str, str], str] = ...) -> str: ...
def urlopen(url: Union[str, urllib.request.Request], data: typing.Optional[bytes] = ..., timeout: typing.Optional[float] = ..., *, cafile: typing.Optional[str] = ..., capath: typing.Optional[str] = ..., cadefault: bool = ..., context: typing.Optional[ssl.SSLContext] = ...) -> typing.Any: ...
