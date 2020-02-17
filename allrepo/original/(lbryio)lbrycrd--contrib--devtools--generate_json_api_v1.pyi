# (generated with --quick)

from typing import Any, Dict, List, Pattern, TypeVar, Union

json: module
re: module
re_argline: Pattern[str]
re_full: Pattern[str]
sp: module
sys: module

_T0 = TypeVar('_T0')
_T1 = TypeVar('_T1')

def get_api(section_name: _T0, command: _T1, command_help) -> Dict[str, Union[str, List[Dict[str, Union[bool, str, List[nothing]]]], _T0, _T1]]: ...
def get_type(arg_type, full_line) -> Any: ...
def parse_params(args) -> List[Dict[str, Union[bool, str, List[nothing]]]]: ...
def process_examples(examples: str) -> List[Dict[str, str]]: ...
def write_api() -> None: ...
