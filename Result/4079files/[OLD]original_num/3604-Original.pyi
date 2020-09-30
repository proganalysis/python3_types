# (generated with --quick)

from typing import Any, Dict, List, Match, Optional, Pattern, Tuple, TypeVar, Union

ESCAPE_CHARS: Dict[str, str]
ParseError: Any
ParseStream: Any
TEST_LINES: Tuple[Tuple[str, List[Tuple[str, Union[int, str]]]], Tuple[str, List[Tuple[str, Union[int, str]]]], Tuple[str, List[Tuple[str, str]]], Tuple[str, List[Tuple[str, Union[str, Dict[str, str]]]]], Tuple[str, List[Tuple[str, Union[int, str, Dict[str, str]]]]], Tuple[str, List[Tuple[str, Union[int, str, Dict[str, str]]]]], Tuple[str, List[Tuple[str, Union[int, str, Dict[str, Union[str, Dict[str, Union[str, List[nothing]]]]]]]]], Tuple[str, List[Tuple[str, str]]], Tuple[str, List[Tuple[str, Union[str, Dict[str, str]]]]], Tuple[str, List[Tuple[str, Union[str, Dict[str, Dict[str, Dict[str, str]]]]]]], Tuple[str, List[Tuple[str, Union[str, Dict[str, List[str]]]]]], Tuple[str, List[Tuple[str, Union[str, Dict[str, Dict[str, str]]]]]], Tuple[str, List[Tuple[str, Optional[str]]]], Tuple[str, List[Tuple[str, Union[int, str, Dict[str, str]]]]], Tuple[str, List[Tuple[str, Union[int, str, Dict[str, str]]]]], Tuple[str, List[Tuple[str, Union[int, str, Dict[str, Union[str, Dict[str, Union[str, List[nothing]]]]]]]]], Tuple[str, List[Tuple[str, Union[str, Dict[str, Dict[str, Dict[str, Union[str, List[Dict[str, str]]]]]]]]]], Tuple[str, List[Tuple[str, Union[str, Dict[str, Dict[str, Dict[str, Union[str, List[nothing]]]]]]]]], Tuple[str, List[Tuple[str, Union[str, Dict[str, Dict[str, str]]]]]], Tuple[str, List[Tuple[str, Union[str, Dict[str, List[Dict[str, str]]]]]]], Tuple[str, List[Tuple[str, Union[str, Dict[str, List[nothing]]]]]]]
attr: Any
expected: Any
key: Any
line: Any
msg: Union[Async, Result, Stream]
value: Any

AnyStr = TypeVar('AnyStr', str, bytes)

class Async:
    EXEC: int
    MAP: Dict[str, int]
    NOTIFY: int
    PATTERN: Pattern[str]
    STATUS: int
    klass: str
    results: Any
    type: int
    def __init__(self, line) -> None: ...
    def __str__(self) -> str: ...

class Result:
    PATTERN: Pattern[str]
    klass: str
    results: Any
    token: int
    def __init__(self, line) -> None: ...

class Stream:
    CONSOLE: int
    ERROR_LOG: int
    MAP: Dict[str, int]
    TARGET: int
    string: Any
    type: int
    def __init__(self, line) -> None: ...

def compile(pattern: Union[Pattern[AnyStr], AnyStr], flags: int = ...) -> Pattern[AnyStr]: ...
def parse(string) -> Union[Async, Result, Stream]: ...
def parse_cstring(s) -> str: ...
def parse_list(s) -> Union[dict, list]: ...
def parse_results(s) -> Dict[str, Any]: ...
def parse_tuple(s) -> dict: ...
def parse_value(s) -> Any: ...
def parse_variable(s) -> str: ...
def search(pattern: Union[Pattern[AnyStr], AnyStr], string: AnyStr, flags: int = ...) -> Optional[Match[AnyStr]]: ...
