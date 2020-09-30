# (generated with --quick)

import enum
import flask.app
import flask.wrappers
from typing import Any, Callable, Iterable, Sequence, Type, TypeVar, Union
import werkzeug.wrappers

CAH_lobby_server: flask.app.Flask
Enum: Type[enum.Enum]
Flask: Type[flask.app.Flask]
Game: Any
GameState: Any
SocketIO: Any
TurnState: Any
add_player: Callable
address: Callable
client_connected: Any
create_expiration_cookie_time: Any
czar: Callable
disconnect: Any
emit: Any
hand: Callable
host: Callable
index: Callable
interrupt: Callable
json: module
judgement: Callable
lobby_state: Callable
login: Callable
os: module
play: Callable
player_count: Callable
request: flask.wrappers.Request
session: Any
shutdown: Callable
socketio: Any
submit_white_card: Any
test_disconnect: Any
test_message: Any
time: module
user: Callable

_RC = TypeVar('_RC', bound=werkzeug.wrappers.Response)

class LobbyState(enum.Enum):
    InGame: int
    WaitingForGameCreation: int
    WaitingForHost: int

def jsonify(*args, **kwargs) -> Any: ...
def make_response(*args) -> Any: ...
@overload
def redirect(location, code: int = ..., Response: None = ...) -> werkzeug.wrappers.Response: ...
@overload
def redirect(location, code: int = ..., Response: Type[_RC] = ...) -> _RC: ...
def render_template(template_name_or_list: Union[str, Iterable[str]], **context) -> str: ...
def shutdown_server() -> None: ...
def with_session(func) -> Callable: ...
def wraps(wrapped: Callable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable[[Callable], Callable]: ...
