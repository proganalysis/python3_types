# (generated with --quick)

import controlevents
import datetime
import enum
import touchhandler
from typing import Any, Dict, List, Optional, Type, Union

CEvent: enum.Enum
ConsoleDetail: Any
ConsoleEvent: Type[controlevents.ConsoleEvent]
clslst: Dict[Any, clsstruct]
collections: module
config: Any
debug: module
doclst: dict
evntcnt: int
exemplarobjs: collections.OrderedDict[Any, List[str]]
globdoc: Dict[nothing, nothing]
hw: module
lastup: Union[float, int]
logsupport: Any
moddoc: Dict[nothing, nothing]
mqttregistered: bool
os: module
paramlog: List[nothing]
previousup: Union[float, int]
pygame: Any
re: module
signal: module
threadmanager: module
timedelta: Type[datetime.timedelta]
ts: Optional[touchhandler.Touchscreen]

class Enumerate(object):
    def __init__(self, names) -> None: ...

class clsstruct:
    membernms: set
    members: List[nothing]
    name: Any
    def __init__(self, nm) -> None: ...
    def addmem(self, nm) -> None: ...

def DumpDocumentation() -> None: ...
def InitializeEnvironment() -> None: ...
def LogParams() -> None: ...
def PostEvent(e) -> None: ...
def get_timedelta(line) -> int: ...
def handler(signum, frame) -> None: ...
def register_example(estr, obj) -> None: ...
