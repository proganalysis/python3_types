# (generated with --quick)

from typing import Any, Dict, List, TextIO, TypeVar, Union

colors: Dict[str, str]
data: Dict[str, Union[str, Dict[str, Union[int, str, Dict[str, Union[int, str]]]], List[Dict[str, Any]]]]
f: TextIO
gem: str
gems: Dict[str, List[Union[float, int]]]
io: module
json: module
stat_names: List[str]

_T0 = TypeVar('_T0')

def get_json(gem: _T0) -> Dict[str, Union[str, Dict[str, Union[int, str, Dict[str, Union[int, str, _T0]]]], List[Dict[str, Any]]]]: ...
