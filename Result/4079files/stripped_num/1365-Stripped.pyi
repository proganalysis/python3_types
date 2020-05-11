# (generated with --quick)

from typing import Any, Dict, Optional, TypeVar

ChampionMasteries: Any
ChampionMastery: Any
ChampionMasteryData: Any
ChampionMasteryDto: Any
ChampionMasteryListData: Any
ChampionMasteryListDto: Any
DataTransformer: Any
PipelineContext: Any

F = TypeVar('F')
T = TypeVar('T')
_T = TypeVar('_T')

class ChampionMasteryTransformer(Any):
    champion_mastery_dto_to_data: Any
    champion_mastery_list_dto_to_data: Any
    transform: Any
    def champion_mastery_data_to_core(self, value, context = ...) -> Any: ...
    def champion_mastery_list_data_to_core(self, value, context = ...) -> Any: ...

def deepcopy(x: _T, memo: Optional[Dict[int, _T]] = ..., _nil = ...) -> _T: ...
