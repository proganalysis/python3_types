# (generated with --quick)

from typing import Any
import unittest.case

Element: Any
Lattice: Any
Poscar: Any
PymatgenTest: Any
RelaxationAnalyzer: Any
Structure: Any
VoronoiAnalyzer: Any
VoronoiConnectivity: Any
Xdatcar: Any
average_coordination_number: Any
contains_peroxide: Any
np: module
os: module
oxide_type: Any
solid_angle: Any
sulfide_type: Any
test_dir: str
unittest: module

class MiscFunctionTest(Any):
    def test_average_coordination_number(self) -> None: ...
    def test_contains_peroxide(self) -> None: ...
    def test_oxide_type(self) -> None: ...
    def test_solid_angle(self) -> None: ...
    def test_sulfide_type(self) -> None: ...

class RelaxationAnalyzerTest(unittest.case.TestCase):
    analyzer: Any
    def test_get_percentage_bond_dist_changes(self) -> None: ...
    def test_vol_and_para_changes(self) -> None: ...

class VoronoiAnalyzerTest(Any):
    _multiprocess_shared_: bool
    s: Any
    ss: Any
    va: Any
    def setUp(self) -> None: ...
    def test_analyze(self) -> None: ...

class VoronoiConnectivityTest(Any):
    def test_connectivity_array(self) -> None: ...
