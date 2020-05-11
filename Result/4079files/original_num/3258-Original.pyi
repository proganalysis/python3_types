# (generated with --quick)

import database
import server
from typing import Any, Callable, Dict, Optional, Type

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
def handler(url: str, method: str = ...) -> Callable[[Any], Any]: ...
def json_post(req: server.RequestHandler) -> Any: ...
def logged_in(req: server.RequestHandler) -> database.db_item: ...
def msg(txt: str) -> str: ...
def post(req: server.RequestHandler) -> Optional[bytes]: ...
def querystring(req: server.RequestHandler) -> dict: ...
