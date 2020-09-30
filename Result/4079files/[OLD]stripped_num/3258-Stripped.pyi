# (generated with --quick)

import server
from typing import Any, Callable, Dict, Type

RequestHandler: Type[server.RequestHandler]
create_dataset_handler: Any
cv2: Any
dataset_get: Any
dataset_list_handler: Any
delete_dataset: Any
get_dataset_status: Any
json: module
keyword_handler: Any
kw: module
nets: module
pending: Dict[Any, Dict[str, Any]]
ts: module

def done_task(task) -> None: ...
def handler(url, method = ...) -> Callable[[Any], Any]: ...
def json_post(req) -> Any: ...
def logged_in(req) -> Any: ...
def msg(txt) -> str: ...
def post(req) -> Any: ...
def querystring(req) -> Dict[Any, list]: ...
