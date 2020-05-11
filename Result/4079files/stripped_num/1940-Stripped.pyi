# (generated with --quick)

from typing import Any
import unittest.case

Agent: Any
DQNAgent: Any
Environment: Any
Image: module
Q: Any
np: module
os: module
shutil: module
sys: module
unittest: module

class FormatAgent(Any):
    _step: int
    agent: Any
    path: Any
    def __init__(self, path) -> None: ...
    def act(self, observation, reward) -> int: ...

class TestDQNAgent(unittest.case.TestCase):
    IMG_PATH: str
    @classmethod
    def setUpClass(cls) -> None: ...
    @classmethod
    def tearDownClass(cls) -> None: ...
    def test_format_image(self) -> None: ...
    def test_save_state(self) -> None: ...
