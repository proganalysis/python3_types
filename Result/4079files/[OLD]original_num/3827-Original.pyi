# (generated with --quick)

from typing import Any, Dict, List, Union

Response: Any
app: Any
asyncio: module
json_response: Any
logging: module
logging_config: Dict[str, Union[int, Dict[str, Dict[str, Union[str, List[str]]]]]]
nginx_500: str
os: module
port: int
random: module
re: module
web: Any

def create_app() -> Any: ...
def mandrill_send_view(request) -> coroutine: ...
def mandrill_sub_account_add(request) -> coroutine: ...
def mandrill_sub_account_info(request) -> coroutine: ...
def mandrill_webhook_add(request) -> coroutine: ...
def mandrill_webhook_list(request) -> coroutine: ...
