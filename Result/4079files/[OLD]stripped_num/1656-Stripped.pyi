# (generated with --quick)

import pch2csd.patch
import pch2csd.resources
from typing import Optional, Type, TypeVar, Union
import unittest.case

Cable: Type[pch2csd.patch.Cable]
CableColor: Type[pch2csd.patch.CableColor]
CableType: Type[pch2csd.patch.CableType]
Location: Type[pch2csd.patch.Location]
Module: Type[pch2csd.patch.Module]
ModuleParameters: Type[pch2csd.patch.ModuleParameters]
ProjectData: Type[pch2csd.resources.ProjectData]
TestCase: Type[unittest.case.TestCase]

_T1 = TypeVar('_T1')

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

def get_test_resource(path) -> str: ...
def parse_pch2(data, pch2_file, convert_in2in = ...) -> pch2csd.patch.Patch: ...
def transform_in2in_cables(patch, cable: _T1) -> Optional[Union[pch2csd.patch.Cable, _T1]]: ...
