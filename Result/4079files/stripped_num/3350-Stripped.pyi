# (generated with --quick)

import numpy
from typing import Any
import unittest.case

doctest: module
metrics: Any
np: module
os: module
parent_dir: str
projections: Any
randn_c: Any
sys: module
unittest: module

class MetricsTestCase(unittest.case.TestCase):
    A: Any
    B: numpy.ndarray
    def test_calc_principal_angles(self) -> None: ...
    def test_calculating_the_chordal_distance(self) -> None: ...

class ProjectionsTestCase(unittest.case.TestCase):
    A: numpy.ndarray
    P_obj: Any
    __doc__: str
    v: numpy.ndarray
    def test_calcOrthogonalProjectionMatrix(self) -> None: ...
    def test_calcProjectionMatrix(self) -> None: ...
    def test_oProject(self) -> None: ...
    def test_project(self) -> None: ...
    def test_reflect(self) -> None: ...

class SubspaceDoctestsTestCase(unittest.case.TestCase):
    __doc__: str
    def test_metrics(self) -> None: ...
    def test_projections(self) -> None: ...
