from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.parsing.custom_config import ConfigObject
from rlbot.utils.structures.game_data_struct import GameTickPacket
from typing import Any

class Atba(BaseAgent):
    flip_turning: bool = ...
    test_rendering: bool = ...
    test_quickchat: bool = ...
    test_dropshot: bool = ...
    test_state: bool = ...
    test_ball_prediction: bool = ...
    test_physics_tick: bool = ...
    cleared: bool = ...
    def get_output(self, game_tick_packet: GameTickPacket) -> SimpleControllerState: ...
    def do_rendering_test(self, game_tick_packet: Any, my_car: Any) -> None: ...
    def do_dropshot_tile_test(self, game_tick_packet: GameTickPacket) -> Any: ...
    def set_state_test(self, game_tick_packet: GameTickPacket) -> Any: ...
    def render_ball_prediction(self) -> None: ...
    def do_physics_tick_test(self, game_tick_packet: GameTickPacket) -> None: ...
    def setup_rainbow(self): ...
    def load_config(self, config_header: Any) -> None: ...
    @staticmethod
    def create_agent_configurations(config: ConfigObject) -> Any: ...

class Vector2:
    x: Any = ...
    y: Any = ...
    def __init__(self, x: float = ..., y: float = ...) -> None: ...
    def __add__(self, val: Any): ...
    def __sub__(self, val: Any): ...
    def correction_to(self, ideal: Any): ...

def get_car_facing_vector(car: Any): ...