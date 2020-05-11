# (generated with --quick)

import collections
from typing import Any, Dict, Type

CentreonServer: Any
IcingaServer: Any
IcingaWeb2Server: Any
LivestatusServer: Any
Monitos3Server: Any
Monitos4xServer: Any
MultisiteServer: Any
NagiosServer: Any
Op5MonitorServer: Any
OpsviewServer: Any
OrderedDict: Type[collections.OrderedDict]
SERVER_TYPES: collections.OrderedDict
STATES: Any
SensuServer: Any
SnagViewServer: Any
ThrukServer: Any
ZabbixServer: Any
ZenossServer: Any
conf: Any
created_server: Any
server: Any
servers: collections.OrderedDict
urllib: module

def create_server(server = ...) -> Any: ...
def get_enabled_servers() -> list: ...
def get_errors() -> bool: ...
def get_status_count() -> Dict[str, Any]: ...
def get_worst_status() -> Any: ...
def register_server(server) -> None: ...
