# (generated with --quick)

from typing import Any
import unittest.case

CBox_v3_driven_transmon: Any
CCL: Any
Dummy_Duplexer: Any
QCC: Any
QWG_driven_transmon: Any
QuDev_transmon: Any
Tektronix_driven_transmon: Any
UHFQC_RO_LutMan: Any
a_tools: Any
approx: Any
ct: Any
do: Any
dummy_CCL: Any
dummy_QCC: Any
dummy_UHFQC: Any
measurement_control: Any
mwl: Any
np: module
openql: Any
openql_import_fail: bool
os: module
pq: Any
sh: Any
station: Any
time: module
unittest: module
v8: Any
vmw: Any
wf: Any

class Test_Device_obj(unittest.case.TestCase):
    @classmethod
    def setUpClass(self) -> None: ...
    @classmethod
    def tearDownClass(self) -> None: ...
    def test_get_dio_map(self) -> None: ...
    def test_prepare_timing_CCL(self) -> None: ...
    def test_prepare_timing_QCC(self) -> None: ...
    def test_prepare_timing_QCC_fine(self) -> None: ...
