# (generated with --quick)

import time
from typing import Any, Dict, List, Match, Optional, Pattern, Tuple, Type, TypeVar, Union
import urllib.parse

CookieType = Tuple[str, str, List[Tuple[str, Union[int, str]]]]

AddNoteMethodType: Any
DELIMITER: str
MONTHS: Dict[str, int]
NON_DELIMITER: str
Note: Any
categories: Any
headers: Any
levels: Any

AnyStr = TypeVar('AnyStr', str, bytes)

class BasicSCTest(Any):
    expected_err: List[nothing]
    expected_out: List[Tuple[str, str, List[nothing]]]
    inputs: List[bytes]
    name: str

class ExpiresScTest(Any):
    expected_err: List[nothing]
    expected_out: List[Tuple[str, str, List[Tuple[str, int]]]]
    inputs: List[bytes]
    name: str

class ExpiresSingleScTest(Any):
    expected_err: List[nothing]
    expected_out: List[Tuple[str, str, List[Tuple[str, int]]]]
    inputs: List[bytes]
    name: str

class MaxAgeLeadingZeroScTest(Any):
    expected_err: List[Type[SET_COOKIE_LEADING_ZERO_MAX_AGE]]
    expected_out: List[Tuple[str, str, List[nothing]]]
    inputs: List[bytes]
    name: str

class MaxAgeScTest(Any):
    expected_err: List[nothing]
    expected_out: List[Tuple[str, str, List[Tuple[str, int]]]]
    inputs: List[bytes]
    name: str

class ParameterSCTest(Any):
    expected_err: List[nothing]
    expected_out: List[Tuple[str, str, List[Tuple[str, str]]]]
    inputs: List[bytes]
    name: str

class RemoveSCTest(Any):
    expected_err: List[nothing]
    expected_out: List[Tuple[str, str, List[Tuple[str, int]]]]
    inputs: List[bytes]
    name: str

class SET_COOKIE_BAD_DATE(Any):
    category: Any
    level: Any
    summary: str
    text: str

class SET_COOKIE_EMPTY_DOMAIN(Any):
    category: Any
    level: Any
    summary: str
    text: str

class SET_COOKIE_EMPTY_MAX_AGE(Any):
    category: Any
    level: Any
    summary: str
    text: str

class SET_COOKIE_LEADING_ZERO_MAX_AGE(Any):
    category: Any
    level: Any
    summary: str
    text: str

class SET_COOKIE_NON_DIGIT_MAX_AGE(Any):
    category: Any
    level: Any
    summary: str
    text: str

class SET_COOKIE_NO_NAME(Any):
    category: Any
    level: Any
    summary: str
    text: str

class SET_COOKIE_NO_VAL(Any):
    category: Any
    level: Any
    summary: str
    text: str

class SET_COOKIE_UNKNOWN_ATTRIBUTE(Any):
    category: Any
    level: Any
    summary: str
    text: str

class TwoSCTest(Any):
    expected_err: List[nothing]
    expected_out: List[Tuple[str, str, List[Tuple[str, str]]]]
    inputs: List[bytes]
    name: str

class WolframSCTest(Any):
    expected_err: List[nothing]
    expected_out: List[Tuple[str, str, List[Tuple[str, Union[int, str]]]]]
    inputs: List[bytes]
    name: str

class set_cookie(Any):
    canonical_name: str
    deprecated: bool
    description: str
    list_header: bool
    nonstandard_syntax: bool
    reference: Any
    syntax: bool
    valid_in_requests: bool
    valid_in_responses: bool
    def parse(self, field_value: str, add_note) -> Tuple[str, str, List[Tuple[str, Union[int, str]]]]: ...

def loose_date_parse(cookie_date: str) -> int: ...
def loose_parse(set_cookie_string: str, uri_path: str, current_time: float, add_note) -> Tuple[str, str, List[Tuple[str, Union[int, str]]]]: ...
def match(pattern: Union[Pattern[AnyStr], AnyStr], string: AnyStr, flags: int = ...) -> Optional[Match[AnyStr]]: ...
def split(pattern: Union[Pattern[AnyStr], AnyStr], string: AnyStr, maxsplit: int = ..., flags: int = ...) -> List[AnyStr]: ...
def timegm(tuple: Union[time.struct_time, Tuple[int, ...]]) -> int: ...
@overload
def urlsplit(url: str, scheme: Optional[str] = ..., allow_fragments: bool = ...) -> urllib.parse.SplitResult: ...
@overload
def urlsplit(url: Optional[bytes], scheme: Optional[bytes] = ..., allow_fragments: bool = ...) -> urllib.parse.SplitResultBytes: ...
