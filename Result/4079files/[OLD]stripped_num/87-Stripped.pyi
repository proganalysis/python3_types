# (generated with --quick)

from typing import Any
import unittest.case

get_test_home_assistant: Any
mochad: Any
mock: module
setup_component: Any
switch: Any
unittest: module

class TestMochadSwitch(unittest.case.TestCase):
    __doc__: str
    hass: Any
    switch: Any
    def teardown_method(self, method) -> None: ...
    def test_name(self) -> None: ...
    def test_turn_off(self) -> None: ...
    def test_turn_on(self) -> None: ...

class TestMochadSwitchSetup(unittest.case.TestCase):
    COMPONENT: Any
    PLATFORM: Any
    THING: str
    __doc__: str
    hass: Any
    test_setup_adds_proper_devices: Any
