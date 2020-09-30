# (generated with --quick)

import qllr.db
from typing import Any, Coroutine, Dict, SupportsFloat

Connection: Any
DATETIME_FORMAT: str
InvalidGametype: Any
MATCH_LIST_ITEM_COUNT: int
PlayerNotFound: Any
cache: qllr.db.Cache
json: module

def ceil(__x: SupportsFloat) -> int: ...
def clean_name(name) -> Any: ...
def get_last_matches(con, gametype = ..., steam_id = ..., page = ..., from_ts = ..., to_ts = ...) -> Coroutine[Any, Any, Dict[str, Any]]: ...
