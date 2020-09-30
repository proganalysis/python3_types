# (generated with --quick)

from typing import Any
import unittest.case

PolarisationFrame: Any
SkyCoord: Any
create_image_from_visibility: Any
create_named_configuration: Any
create_pb: Any
create_visibility: Any
create_vp: Any
create_vp_generic_numeric: Any
export_image_to_fits: Any
log: logging.Logger
logging: module
numpy: module
plt: Any
show_image: Any
u: Any
unittest: module

class TestPrimaryBeams(unittest.case.TestCase):
    channel_bandwidth: numpy.ndarray
    config: Any
    dir: Any
    flux: numpy.ndarray
    frequency: Any
    phasecentre: Any
    times: Any
    vis: Any
    def createVis(self, config = ..., dec = ..., rmax = ..., freq = ...) -> None: ...
    def test_create_voltage_patterns_zernike(self) -> None: ...
