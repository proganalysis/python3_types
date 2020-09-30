# (generated with --quick)

from typing import Any
import unittest.case

PolarisationFrame: Any
SkyCoord: Any
Skycomponent: Any
create_blockvisibility: Any
create_image: Any
create_named_configuration: Any
create_pointingtable_from_blockvisibility: Any
create_vp: Any
log: logging.Logger
logging: module
numpy: module
simulate_gaintable_from_pointingtable: Any
simulate_pointingtable_from_timeseries: Any
u: Any
unittest: module

class TestPointing(unittest.case.TestCase):
    channel_bandwidth: numpy.ndarray
    dir: Any
    doplot: bool
    frequency: numpy.ndarray
    midcore: Any
    model: Any
    nants: int
    ntimes: int
    phasecentre: Any
    times: Any
    vis: Any
    def test_simulate_gaintable_from_time_series(self) -> None: ...
