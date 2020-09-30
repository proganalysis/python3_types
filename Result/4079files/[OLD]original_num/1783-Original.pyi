# (generated with --quick)

from typing import AbstractSet, Any, Coroutine, Dict, Optional, Tuple

JSONDict = Dict[str, Any]

CLA_OK: str
EASTEREGG_PROBABILITY: float
GITHUB_EMAIL: str
GitHubAPI: Any
JSON: Any
LABEL_PREFIX: str
NO_CLA: str
NO_CLA_BODY: str
NO_CLA_BODY_EASTEREGG: str
NO_CLA_TEMPLATE: str
NO_USERNAME_BODY: str
aiohttp: Any
asyncio: module
enum: module
http: module
ni_abc: Any
random: module
sansio: Any
uritemplate: Any
web: Any

class Host(Any):
    __doc__: str
    _gh: Any
    _useful_actions: set
    event: PullRequestEvent
    request: Dict[str, Any]
    route: Tuple[str, str]
    server: Any
    def __init__(self, server, client, event: PullRequestEvent, request: Dict[str, Any]) -> None: ...
    def comment(self, status) -> Coroutine[Any, Any, Optional[str]]: ...
    def current_label(self) -> Coroutine[Any, Any, Optional[str]]: ...
    def labels_url(self, label: Optional[str] = ...) -> Coroutine[Any, Any, str]: ...
    @classmethod
    def process(cls, server, request, client) -> Coroutine[Any, Any, Host]: ...
    def remove_label(self) -> Coroutine[Any, Any, Optional[str]]: ...
    def set_label(self, status) -> Coroutine[Any, Any, str]: ...
    def update(self, status) -> Coroutine[Any, Any, None]: ...
    def usernames(self) -> Coroutine[Any, Any, AbstractSet[str]]: ...

class PullRequestEvent(enum.Enum):
    assigned: str
    closed: str
    labeled: str
    opened: str
    reopened: str
    synchronize: str
    unassigned: str
    unlabeled: str
