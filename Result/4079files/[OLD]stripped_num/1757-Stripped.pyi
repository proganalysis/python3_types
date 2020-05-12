# (generated with --quick)

import collections
import itertools
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

base64: module
chain: Type[itertools.chain]
combine_keys: List[Tuple[str, ...]]
datetime: module
defaultdict: Type[collections.defaultdict]
pickle: module
requests: module
time: module
tqdm: Any
xref_keys: List[str]

_T0 = TypeVar('_T0')

def alwayslist(value: _T0) -> Union[List[_T0], _T0]: ...
def download_stitcher() -> list: ...
def load_parsed_data() -> Any: ...
def main() -> None: ...
def organize_data(contents) -> dict: ...
def organize_one_record(d) -> List[Dict[str, Any]]: ...
