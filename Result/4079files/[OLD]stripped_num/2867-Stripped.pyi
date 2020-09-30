# (generated with --quick)

from typing import Any, Tuple, TypeVar

CrystallographicMap: Any
_distance_from_fixed_angle: Any
dp_cryst_map: Any
dp_cryst_map_vector: Any
euler2quat: Any
load_mtex_map: Any
mod_cryst_map: Any
np: module
os: module
pytest: Any
qinverse: Any
qmult: Any
quat2axangle: Any
sp_cryst_map: Any

_T0 = TypeVar('_T0')

class TestMTEXIO:
    def test_Crystallographic_Map_io(self, dp_cryst_map) -> None: ...

class TestMapCreation:
    test_get_metric_map_no_method: Any
    test_get_metric_map_template_match: Any
    test_get_metric_map_template_match_bad_metric: Any
    test_get_metric_map_vector_match: Any
    test_get_metric_map_vector_match_bad_metric: Any
    def test_get_orientation_map(self, sp_cryst_map) -> None: ...
    def test_get_phase_map(self, sp_cryst_map) -> None: ...

class TestModalAngularFunctionality:
    def test_get_distance_from_fixed_angle(self) -> None: ...
    def test_get_distance_from_modal(self, mod_cryst_map) -> None: ...
    def test_get_modal_angles(self, mod_cryst_map) -> None: ...

def get_distance_between_two_angles_longform(angle_1, angle_2) -> Any: ...
def worker_for_test_CrystallographicMap_io(mapp: _T0) -> Tuple[_T0, Any]: ...
