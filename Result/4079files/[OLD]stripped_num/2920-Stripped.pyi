# (generated with --quick)

import numpy
from typing import Any, Dict, List, Tuple, Type, Union
import unittest.case

CircleProfile: Any
CollapsedCircleProfile: Any
MultiProfile: Any
SingleProfile: Any
TestCase: Type[unittest.case.TestCase]
image: Any
np: module
osp: module
sps: Any

class CircleProfileStarshot(CircleProfileTestMixin, unittest.case.TestCase):
    fwxm_peak_idxs: List[float]
    peak_idxs: List[float]
    valley_idxs: List[float]

class CircleProfileTestMixin:
    center_point: Tuple[int, int]
    fwxm_peak_idxs: Tuple[int]
    image_file_location: str
    klass: Any
    peak_idxs: Tuple[int]
    radius: int
    valley_idxs: Tuple[int]
    @classmethod
    def setUpClass(cls) -> None: ...
    def test_add_to_axes(self) -> None: ...
    def test_fwxm_peak_idxs(self) -> None: ...
    def test_locations(self) -> None: ...
    def test_peak_idxs(self) -> None: ...
    def test_valley_idxs(self) -> None: ...

class CollapsedCircleProfileStarshot(CircleProfileTestMixin, unittest.case.TestCase):
    fwxm_peak_idxs: List[float]
    klass: Any
    peak_idxs: List[float]
    valley_idxs: List[float]

class MultiProfileTestMixin:
    peak_fwxm_idxs: Tuple[int]
    peak_max_idxs: Tuple[int]
    subdivide_fwxm_centers: Tuple[int]
    valley_max_idxs: Tuple[int]
    values: Type[numpy.ndarray]
    @classmethod
    def setUpClass(cls) -> None: ...
    def test_find_fwxm_peaks(self) -> None: ...
    def test_find_peaks(self) -> None: ...
    def test_find_valleys(self) -> None: ...
    def test_subdivide(self) -> None: ...

class MultiProfileTriangle(MultiProfileTestMixin, unittest.case.TestCase):
    peak_fwxm_idxs: Tuple[int, int, int, int]
    peak_max_idxs: Tuple[int, int, int, int]
    subdivide_fwxm_centers: Tuple[int, int, int, int]
    valley_max_idxs: Tuple[int, int, int]
    values: Any
    x_values: Any
    def test_ground_profile(self) -> None: ...

class SingleProfileCutoffTriangle(SingleProfileMixin, unittest.case.TestCase):
    __doc__: str
    field_calculations: Dict[str, float]
    field_edge_indices: Tuple[int, int]
    field_value_length: int
    fwxm_center_indices: Dict[int, Union[float, int]]
    fwxm_center_values: Dict[int, float]
    fwxm_indices: Dict[int, int]
    peak_idx: int
    penumbra_widths_8020: Dict[str, Union[float, int]]
    penumbra_widths_9010: Dict[str, Union[float, int]]
    xdata: Any
    ydata: Any

class SingleProfileMixin:
    field_calculations: Dict[str, int]
    field_edge_indices: Tuple[int, int]
    field_value_length: int
    fwxm_center_indices: Dict[int, int]
    fwxm_center_values: Dict[int, int]
    fwxm_indices: Dict[int, int]
    normalize_sides: bool
    peak_idx: int
    penumbra_widths_8020: Dict[str, int]
    penumbra_widths_9010: Dict[str, int]
    ydata: Type[numpy.ndarray]
    @classmethod
    def setUpClass(cls) -> None: ...
    def test_field_calculations(self) -> None: ...
    def test_field_edges(self) -> None: ...
    def test_field_value_length(self) -> None: ...
    def test_fwxm_centers(self) -> None: ...
    def test_fwxms(self) -> None: ...
    def test_initial_peak(self) -> None: ...
    def test_penum_widths(self) -> None: ...
    def test_unnormalized_peaks(self) -> None: ...

class SingleProfileTriangle(SingleProfileMixin, unittest.case.TestCase):
    field_calculations: Dict[str, float]
    field_edge_indices: Tuple[int, int]
    field_value_length: int
    fwxm_center_indices: Dict[int, int]
    fwxm_center_values: Dict[int, int]
    fwxm_indices: Dict[int, int]
    peak_idx: int
    penumbra_widths_8020: Dict[str, int]
    penumbra_widths_9010: Dict[str, int]
    xdata: Any
    ydata: Any
