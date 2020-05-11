# (generated with --quick)

import collections
from typing import Any, Dict, List, Optional, Set, SupportsFloat, Tuple, Type, TypeVar, Union

ENGLISH_INDEX: Any
GOOD_HEIGHTS: Any
GOOD_SUBFOLDERS: List[str]
OrderedDict: Type[collections.OrderedDict]
VideoGroup: Any
glob: module
json: module
os: module
probe_video: Any

_T1 = TypeVar('_T1')

def check(target, prefix) -> list: ...
def check_dirs(*, dirs = ..., output_dir = ..., prefix = ..., partial = ...) -> Optional[bool]: ...
def check_final(*, dirs = ..., output_dir = ...) -> None: ...
def check_group(target_dir, prefix, target_ext = ...) -> Union[Dict[nothing, nothing], Tuple[Any, Dict[str, Dict[str, Union[float, int, List[Dict[str, Union[bool, float, Dict[str, Any]]]], Set[int]]]]]]: ...
def floor(__x: SupportsFloat) -> int: ...
def format_results(results, partial: _T1 = ...) -> collections.OrderedDict[str, Optional[Union[collections.OrderedDict[Any, collections.OrderedDict[Any, collections.OrderedDict[str, Any]]], _T1]]]: ...
def post_merge_check(check_file) -> None: ...
