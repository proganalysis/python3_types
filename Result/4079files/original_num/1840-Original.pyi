# (generated with --quick)

from typing import Any, Dict, Optional, Type

User: Type[str]
abort: Any
check_credentials: Any
comb: module
fetch_static: Any
get: Any
logged_in_users: Dict[bytes, Any]
post: Any
post_message: Any
pubsub: module
request: Any
response: Any
run: Any
secret: str
secrets: module
session: Any
show_followers: Any
show_following: Any
show_main_page: Any
show_search: Any
show_user_page: Any
static_file: Any
template: Any
view: Any

def get_logged_in_user() -> Optional[str]: ...
def verify_user_exists(user) -> None: ...
