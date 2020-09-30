# (generated with --quick)

from typing import Any, Dict

FriendFilter: Any
_ApiResourceBase: Any
_EnumBase: Any

class CurrentUser(Any):
    __doc__: str
    _iface: Any
    behind_nat: Any
    level: Any
    logged_in: Any
    steam_handle: Any
    steam_id: Any
    user: User
    def __init__(self, *args, **kwargs) -> None: ...
    def __str__(self) -> str: ...

class User(Any):
    __doc__: str
    _iface: Any
    _iface_user: Any
    level: Any
    name: Any
    name_history: list
    nickname: Any
    state: Any
    user_id: Any
    def __init__(self, user_id, *args, **kwargs) -> None: ...
    def __str__(self) -> str: ...
    def accept_friend_invite(self) -> None: ...
    def add_to_friends(self) -> None: ...
    def get_state(self, as_str = ...) -> Any: ...
    def has_friends(self, flt = ...) -> Any: ...
    def ignore_friend_invite(self) -> None: ...
    def open_chat(self) -> None: ...
    def open_trade(self) -> None: ...
    def remove_from_friends(self) -> None: ...
    def show_achievements(self) -> None: ...
    def show_profile(self) -> None: ...
    def show_stats(self) -> None: ...

class UserState(Any):
    AWAY: int
    BUSY: int
    MAX: int
    OFFLINE: int
    ONLINE: int
    READY_TO_PLAY: int
    READY_TO_TRADE: int
    SNOOZE: int
    __doc__: str
    aliases: Dict[int, str]
