# (generated with --quick)

from typing import Any, List

NotificationDispatcher: Any
School: Any
json: module
logging: module
os: module
sys: module
textwrap: module
threading: module
time: module
tweepy: Any

class TweetQueue(threading.Thread):
    dispatcher: Any
    queue: List[str]
    def __init__(self, dispatcher) -> None: ...
    def run(self) -> Any: ...

class TwitterDispatcher(Any):
    api: Any
    auth: Any
    config: Any
    dispatcher_name: str
    logger: logging.Logger
    queue: TweetQueue
    def __init__(self) -> None: ...
    def dispatch_notification(self, school, new_status) -> None: ...
