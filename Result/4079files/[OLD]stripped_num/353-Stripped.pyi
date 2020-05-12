# (generated with --quick)

import io
from typing import Any, List, Type, TypeVar, Union

BytesIO: Type[io.BytesIO]
FieldFile: Any
Form: Any
StringIO: Type[io.StringIO]
csv: module
os: module
zipfile: module

_T1 = TypeVar('_T1')

def _get_rows(form) -> List[list]: ...
def _write_csv(form, stream: _T1) -> _T1: ...
def files_zip(files, folder = ...) -> io.BytesIO: ...
def write_zip(forms, stream: _T1 = ..., folder = ...) -> Union[io.BytesIO, _T1]: ...
