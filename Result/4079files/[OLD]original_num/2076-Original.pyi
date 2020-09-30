# (generated with --quick)

import __future__
import collections
import dateutil.parser
from typing import Any, Dict, Generator, IO, Optional, Type, TypeVar, Union

HttpSite: Any
OrderedDict: Type[collections.OrderedDict]
absolute_import: __future__._Feature
datetime: module
json: module
re: module
timeParser: Any
urllib: module

_T1 = TypeVar('_T1')
_T3 = TypeVar('_T3')

class JsonApi(Any):
    def get_json(self, url = ...) -> Any: ...
    @classmethod
    def get_result_dicts(cls, data: _T1, parser, mm_key: _T3 = ..., onlyif = ...) -> Generator[Union[collections.OrderedDict, Dict[Any, _T3], _T1], Any, None]: ...
    @staticmethod
    def get_value(data, key, default = ...) -> Any: ...
    @classmethod
    def multi_match_generator(cls, data, parser, mm_key) -> Generator[Any, Any, None]: ...
    def parse_dict(self, data, parser) -> Generator[Any, Any, None]: ...
    def run(self) -> Generator[Any, Any, None]: ...

def parse(timestr: Union[bytes, str, IO], parserinfo: Optional[dateutil.parser.parserinfo] = ..., **kwargs) -> datetime.datetime: ...
