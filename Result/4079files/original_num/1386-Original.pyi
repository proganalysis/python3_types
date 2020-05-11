# (generated with --quick)

from typing import Any
import unittest.case

KubeNode: Any
KubePod: Any
capacity: Any
os: module
pykube: Any
unittest: module
yaml: module

class TestCapacity(unittest.case.TestCase):
    api: Any
    dummy_node: Any
    dummy_pod: Any
    def test_can_fit(self) -> None: ...
    def test_impossible(self) -> None: ...
    def test_possible(self) -> None: ...
