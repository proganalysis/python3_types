# (generated with --quick)

import _csv
from typing import Any, BinaryIO, Dict, List, TextIO, Type, Union

address: Dict[str, Union[bool, str]]
city: Union[bool, str]
classification: Union[bool, str]
csv: module
data: List[Dict[str, Union[bool, str, Dict[str, Union[bool, str]]]]]
datetime: Type[datetime.datetime]
fqhc: Dict[str, Union[bool, str, Dict[str, Union[bool, str]]]]
fqhcName: Union[bool, str]
headers: List[str]
importfile: TextIO
importfilereader: _csv._reader
json: module
line1: Union[bool, str]
noimportcsvfile: BinaryIO
noimportwriter: _csv._writer
outfile: TextIO
phone: Union[bool, str]
re: module
row: List[str]
state: Union[bool, str]
website: Union[bool, str]
zip: Union[bool, str]

def isNotEmptyAfterStrip(data) -> Any: ...
def processPhone(number) -> str: ...
