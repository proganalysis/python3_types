# (generated with --quick)

from typing import Any, TypeVar

BOT_CONFIG_AGENT_HEADER: Any
BallState: Any
BaseAgent: Any
BoostState: Any
CarState: Any
ConfigObject: Any
DropshotTileState: Any
GameInfoState: Any
GameState: Any
GameTickPacket: Any
Physics: Any
QuickChats: Any
Rotator: Any
SimpleControllerState: Any
Vector3: Any
math: module

_TVector2 = TypeVar('_TVector2', bound=Vector2)

class Atba(Any):
    cleared: bool
    flip_turning: Any
    test_ball_prediction: Any
    test_dropshot: Any
    test_physics_tick: Any
    test_quickchat: Any
    test_rendering: Any
    test_state: Any
    @staticmethod
    def create_agent_configurations(config) -> None: ...
    def do_dropshot_tile_test(self, game_tick_packet) -> None: ...
    def do_physics_tick_test(self, game_tick_packet) -> None: ...
    def do_rendering_test(self, game_tick_packet, my_car) -> None: ...
    def get_output(self, game_tick_packet) -> Any: ...
    def load_config(self, config_header) -> None: ...
    def render_ball_prediction(self) -> None: ...
    def set_state_test(self, game_tick_packet) -> None: ...
    def setup_rainbow(self) -> list: ...

class Vector2:
    x: float
    y: float
    def __add__(self: _TVector2, val) -> _TVector2: ...
    def __init__(self, x = ..., y = ...) -> None: ...
    def __sub__(self: _TVector2, val) -> _TVector2: ...
    def correction_to(self, ideal) -> float: ...

def get_car_facing_vector(car) -> Vector2: ...
