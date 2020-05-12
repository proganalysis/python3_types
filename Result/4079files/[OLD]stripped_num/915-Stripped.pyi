# (generated with --quick)

from typing import Any, Tuple, TypeVar

_io: Any
datetime: module

_T0 = TypeVar('_T0')

def add_timestamp(entry) -> str: ...
def get_timestamp(entry) -> Any: ...
def read_wo_timestamps(entries) -> list: ...
def remove_timestamp(entry) -> Any: ...
def timetuple(entry: _T0) -> Tuple[_T0, datetime.datetime]: ...
def write_with_timestamps(file, entries) -> None: ...
