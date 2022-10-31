# (generated with --quick)

from typing import Any, Tuple, Union

IRC_RATE_LIMIT: float
RECONNECT_MAX_INTERVAL: int
RECONNECT_MIN_INTERVAL: int
_logger: logging.Logger
argparse: module
datetime: module
enum: module
irc: Any
json: module
logging: module
random: module
re: module
ssl: module
time: module

class BattleState(enum.Enum):
    battle: str
    betting: str
    finished: str
    waiting: str

class BetBot(object):
    MIN_BALANCE: int
    TIER_BALANCE_THRESHOLD: Tuple[int, int, int, int, int, int]
    TIER_BET_CHANCES: Tuple[float, float, float, float, float, float]
    TIER_BUY_PRICES: Tuple[Tuple[int], Tuple[int, int, int, int, int, int, int, int, int, int], Tuple[int, int, int, int, int, int, int, int, int, int], Tuple[int, int, int, int, int, int, int, int, int, int], Tuple[int, int, int, int, int, int, int, int, int, int], Tuple[int, int, int, int, int, int, int, int, int, int]]
    TIER_SELL_PRICES: Tuple[Tuple[int, ...], ...]
    _battle_state: Any
    _bet_placed: bool
    _cool_off_timestamp: Union[float, int]
    _token_balance: Any
    _tpp_bot: Any
    def __init__(self, tpp_bot) -> None: ...
    def _place_bet(self, tier_index) -> None: ...
    def reset(self, soft = ...) -> None: ...
    def set_token_balance(self, tokens) -> None: ...
    def start_battle(self) -> None: ...
    def start_betting(self) -> None: ...
    def stop_battle(self) -> None: ...

class Client(Any):
    _bet_bot: BetBot
    _reconnect_interval: int
    _running: bool
    _tpp_bot_facade: TPPBotFacade
    def __init__(self) -> None: ...
    def _keep_alive(self) -> None: ...
    def _process_message(self, event) -> None: ...
    def _schedule_reconnect(self) -> None: ...
    def autoconnect(self, *args, **kwargs) -> None: ...
    def on_action(self, connection, event) -> None: ...
    def on_disconnect(self, connection, event) -> None: ...
    def on_pubmsg(self, connection, event) -> None: ...
    def on_welcome(self, connection, event) -> None: ...
    def on_whisper(self, connection, event) -> None: ...
    def stop(self) -> None: ...

class TPPBotFacade(object):
    _client: Any
    def __init__(self, client) -> None: ...
    def _send_tpp_bot_whisper(self, command) -> None: ...
    def get_balance(self) -> None: ...
    def place_buy_order(self, team, price = ..., amount = ..., duration = ...) -> None: ...
    def place_sell_order(self, team, price = ..., amount = ..., duration = ...) -> None: ...

def main() -> None: ...