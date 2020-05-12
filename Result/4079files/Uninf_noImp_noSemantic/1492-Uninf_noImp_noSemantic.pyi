import hug
from typing import Any

__version__: str
QUERY: str
SERVER: str
PROTOCOL: Any
PORT: Any
REQUEST_TEMPLATE: Any
HISTORY_TEMPLATE: str
COMMAND_TEMPLATE: str
CACHE_REFRESH: Any
executable: Any

def pipeline(hostname: Any, port: Any, path_list: Any, headers: Any = ...): ...
def chunks(l: Any, n: Any) -> None: ...
def generateHeaders(referer: Any): ...
def set_default(obj: Any): ...
def getDataMinimal(minx: hug.types.float_number, miny: hug.types.float_number, maxx: hug.types.float_number, maxy: hug.types.float_number, referer: Any=...) -> Any: ...

featuresTime: Any
features: Any

def getData(minx: hug.types.float_number, miny: hug.types.float_number, maxx: hug.types.float_number, maxy: hug.types.float_number, referer: Any=...) -> Any: ...
