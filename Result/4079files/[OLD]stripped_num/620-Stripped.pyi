# (generated with --quick)

from typing import Any, Dict

BallPlacement: Any
BambaFollow: Any
DefenseWall: Any
DefenseWallNoKick: Any
DirectFreeKick: Any
DoNothing: Any
HumanControl: Any
IndianaJones: Any
IndirectFreeKick: Any
LineUp: Any
Offense: Any
OffenseKickOff: Any
PassesWithDecisions: Any
PathfinderBenchmark: Any
PenaltyDefense: Any
PenaltyOffense: Any
PrepareKickOffDefense: Any
PrepareKickOffOffense: Any
PreparePenaltyDefense: Any
PreparePenaltyOffense: Any
RobocupChoreography: Any
SmartStop: Any
StayAway: Any
Strategy: Any
TestGoalKeeper: Any
TestPassing: Any
__author__: str
logging: module

class StrategyBook:
    default_strategies: list
    logger: logging.Logger
    stop_strategy: Any
    strategies_name: list
    strategies_roles: Dict[Any, Dict[str, list]]
    strategy_book: dict
    def __init__(self) -> None: ...
    def check_existance_strategy(self, strategy_name) -> bool: ...
    def get_strategy(self, strategy_name) -> Any: ...
