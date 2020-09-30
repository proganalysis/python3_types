# (generated with --quick)

from typing import Any, Dict, List

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
    strategies_name: List[str]
    strategies_roles: Dict[str, Dict[str, List[str]]]
    strategy_book: dict
    def __init__(self) -> None: ...
    def check_existance_strategy(self, strategy_name: str) -> bool: ...
    def get_strategy(self, strategy_name: str) -> type: ...
