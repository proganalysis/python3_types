# (generated with --quick)

from typing import Any, List, MutableMapping, Optional

Mastodon: Any
arrow: Any
logger: logging.Logger
logging: module
lxml: module
os: module
requests: module
sys: module
time: module
toml: module

class PyborgMastodon(object):
    __doc__: str
    last_look: Any
    mastodon: Any
    multi_server: Any
    multiplexing: bool
    my_id: Any
    settings: MutableMapping[str, Any]
    toml_file: Any
    def __init__(self, conf_file) -> None: ...
    def handle_toots(self, toots: List[dict]) -> None: ...
    def is_reply_to_me(self, item: dict) -> bool: ...
    def learn(self, body) -> None: ...
    def reply(self, body) -> Optional[str]: ...
    def should_reply_direct(self, usern) -> bool: ...
    def start(self, folder = ...) -> None: ...
    def teardown(self) -> None: ...
