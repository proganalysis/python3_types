# (generated with --quick)

from typing import Any
import unittest.case

CosineDistance: Any
EuclideanDistance: Any
ManhattanDistance: Any
numpy: module
scipy: Any
unittest: module

class TestCosineDistance(unittest.case.TestCase):
    cosine: Any
    def test_symmetry(self) -> None: ...

class TestEuclideanDistance(unittest.case.TestCase):
    euclidean: Any
    def test_symmetry(self) -> None: ...
    def test_triangle_inequality(self) -> None: ...

class TestManhattanDistance(unittest.case.TestCase):
    manhattan: Any
    def test_symmetry(self) -> None: ...
    def test_triangle_inequality(self) -> None: ...

def check_distance_symmetry(test_obj, distance) -> None: ...
def check_distance_triangle_inequality(test_obj, distance) -> None: ...
