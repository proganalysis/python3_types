# (generated with --quick)

import collections
import json.decoder
import json.encoder
from typing import Any, Dict, Pattern, Type, TypeVar, Union

OrderedDict: Type[collections.OrderedDict]
UserDict: Any
decoded_json: Any
encoded_json: str
json: module
numbers: module
re: module

_T0 = TypeVar('_T0')

class ConnectionDecoder(json.decoder.JSONDecoder):
    regex_str_tuple: Pattern[str]
    def __init__(self, *args, **kwargs) -> None: ...
    def decode(self, o) -> Any: ...
    def default(self, obj: _T0) -> Union[list, Dict[nothing, nothing], _T0]: ...
    def my_decode(self, obj: _T0, escape_keys = ...) -> Union[list, Dict[nothing, nothing], _T0]: ...

class ConnectionEncoder(json.encoder.JSONEncoder):
    def default(self, obj) -> Any: ...
    def my_encode(self, obj, escape_keys = ...) -> Any: ...

class JSONStrMixin:
    def __str__(self) -> str: ...
    def to_json(self) -> str: ...
