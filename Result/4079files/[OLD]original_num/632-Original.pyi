# (generated with --quick)

from typing import Any, List, Tuple

BOT_INFO: str
COMP_URL: str
DCI_API_ID: str
ORG_URL: str
client_id: Any
client_secret: Any
json: module
password: Any
praw: Any
requests: module
show_file: Any
username: Any

class WebBot(object):
    __agent__: str
    __doc__: str
    conn: Any
    show_file: Any
    subreddit: str
    def __init__(self, subreddit: str = ...) -> None: ...
    def _parse_show_info(self, show_guid: str) -> Tuple[str, str]: ...
    def _parse_show_recap(self, show_rounds: List[dict]) -> str: ...
    def connect(self) -> None: ...
    def get_show_list(self) -> List[dict]: ...
    def post_thread(self, show_info: dict) -> None: ...
