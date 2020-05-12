# (generated with --quick)

import collections
from typing import Any, Callable, Dict, Iterable, Sized, Tuple, Type, TypeVar, Union

enum: module

_Tnamedtuple-PredefinedOptions-app_id-context_id = TypeVar('_Tnamedtuple-PredefinedOptions-app_id-context_id', bound=`namedtuple-PredefinedOptions-app_id-context_id`)

class Asset:
    amount: Any
    asset_id: Any
    game: Any
    def __init__(self, asset_id, game, amount = ...) -> None: ...
    def to_dict(self) -> Dict[str, Any]: ...

class Currency(enum.IntEnum):
    CHF: int
    EURO: int
    GBP: int
    USD: int

class Endpoints:
    CHAT_LOGIN: str
    CHAT_LOGOUT: str
    CHAT_POLL: str
    SEND_MESSAGE: str

class GameOptions:
    CS: `namedtuple-PredefinedOptions-app_id-context_id`
    DOTA2: `namedtuple-PredefinedOptions-app_id-context_id`
    PUBG: `namedtuple-PredefinedOptions-app_id-context_id`
    PredefinedOptions: Type[`namedtuple-PredefinedOptions-app_id-context_id`]
    STEAM: `namedtuple-PredefinedOptions-app_id-context_id`
    TF2: `namedtuple-PredefinedOptions-app_id-context_id`
    app_id: Any
    context_id: Any
    def __init__(self, app_id, context_id) -> None: ...

class SteamUrl:
    API_URL: str
    COMMUNITY_URL: str
    STORE_URL: str

class TradeOfferState(enum.IntEnum):
    Accepted: int
    Active: int
    Canceled: int
    CanceledBySecondaryFactor: int
    ConfirmationNeed: int
    Countered: int
    Declined: int
    Expired: int
    Invalid: int
    InvalidItems: int
    StateInEscrow: int

class `namedtuple-PredefinedOptions-app_id-context_id`(tuple):
    __slots__ = ["app_id", "context_id"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str]
    app_id: Any
    context_id: Any
    def __getnewargs__(self) -> Tuple[Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-PredefinedOptions-app_id-context_id`], app_id, context_id) -> `_Tnamedtuple-PredefinedOptions-app_id-context_id`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-PredefinedOptions-app_id-context_id`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-PredefinedOptions-app_id-context_id`: ...
    def _replace(self: `_Tnamedtuple-PredefinedOptions-app_id-context_id`, **kwds) -> `_Tnamedtuple-PredefinedOptions-app_id-context_id`: ...

def namedtuple(typename: str, field_names: Union[str, Iterable[str]], *, verbose: bool = ..., rename: bool = ...) -> type: ...
