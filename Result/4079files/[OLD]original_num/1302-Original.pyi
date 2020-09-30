# (generated with --quick)

from typing import Any

CEvent: Any
ConsoleEvent: Any
PostEvent: Any
RegisterDomain: Any
StatefulHAnode: Any
_NormalizeState: Any
debug: Any
ha: Any

class Light(Any):
    internalstate: Any
    def SendOnOffCommand(self, settoon) -> None: ...
    def Update(self, **ns) -> None: ...
    def __init__(self, HAitem, d) -> None: ...
