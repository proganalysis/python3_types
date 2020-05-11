# (generated with --quick)

import requests.sessions
from typing import Any, Dict, List

grequests: Any
math: module
re: module
requests: module
sess: requests.sessions.Session

def _load_n_items(feed: str, max_news_items: int) -> Any: ...
def get_news(feed: str = ..., max_news_items: int = ...) -> List[Dict[str, Any]]: ...
