# (generated with --quick)

import pch2csd.patch
import pch2csd.resources
from typing import Optional, Type
import unittest.case

Cable: Type[pch2csd.patch.Cable]
CableColor: Type[pch2csd.patch.CableColor]
CableType: Type[pch2csd.patch.CableType]
Location: Type[pch2csd.patch.Location]
Module: Type[pch2csd.patch.Module]
ModuleParameters: Type[pch2csd.patch.ModuleParameters]
ProjectData: Type[pch2csd.resources.ProjectData]
TestCase: Type[unittest.case.TestCase]

class TestCableTracing(unittest.case.TestCase):
    data: pch2csd.resources.ProjectData
    def test_in2in__all_cables_from_the_first_module(self) -> None: ...

class TestModes(unittest.case.TestCase):
    data: pch2csd.resources.ProjectData
    def test_modes__LfoC(self) -> None: ...

class TestParsing(unittest.case.TestCase):
    data: pch2csd.resources.ProjectData
    def test_gleb2_pch(self) -> None: ...
    def test_gleb2_pch__unequal(self) -> None: ...

def get_test_resource(path: str) -> str: ...
def parse_pch2(data: pch2csd.resources.ProjectData, pch2_file: str, convert_in2in = ...) -> pch2csd.patch.Patch: ...
def transform_in2in_cables(patch: pch2csd.patch.Patch, cable: pch2csd.patch.Cable) -> Optional[pch2csd.patch.Cable]: ...
