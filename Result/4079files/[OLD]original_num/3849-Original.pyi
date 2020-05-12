# (generated with --quick)

import json.decoder
import json.encoder
from typing import Type, TypeVar, Union

datetime: Type[datetime.datetime]
json: module

_T0 = TypeVar('_T0')

class DictOrDateTime(json.encoder.JSONEncoder): ...

class ReservationDecoder(json.decoder.JSONDecoder):
    def __init__(self, *args, **kwargs) -> None: ...
    def object_hook(self, obj: _T0) -> Union[datetime.datetime, _T0]: ...

class SimpleDict(json.encoder.JSONEncoder): ...
