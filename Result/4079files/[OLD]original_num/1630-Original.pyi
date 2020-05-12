# (generated with --quick)

import _csv
from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Type, TypeVar, Union

csv: module
data: List[Dict[str, Optional[Union[str, Dict[Union[int, str], Union[bool, str, Dict[str, Union[bool, str]]]]]]]]
dateVerified: str
dateVerifiedObj: Dict[str, Union[bool, str]]
dateVerifiedSplit: List[str]
datetime: Type[datetime.datetime]
headers: List[str]
hours: Dict[int, Dict[str, Union[bool, str]]]
i: int
importfile: TextIO
importfilereader: _csv._reader
json: module
noimportcsvfile: BinaryIO
noimportwriter: _csv._writer
outfile: TextIO
pregnancyCenter: Dict[str, Optional[Union[str, Dict[Union[int, str], Union[bool, str, Dict[str, Union[bool, str]]]]]]]
re: module
row: List[str]
services: Dict[str, bool]
valid_services: Dict[str, str]

_T0 = TypeVar('_T0')

def processAddress(str_address: _T0) -> Dict[str, Any]: ...
def processOpenClose(openclose) -> Dict[str, Union[bool, str]]: ...
def processPhone(phone, prcName) -> Optional[str]: ...
def processTime(rawtime, close = ...) -> str: ...
