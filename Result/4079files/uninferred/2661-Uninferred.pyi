import unittest
from typing import Any

def check_distance_symmetry(test_obj: Any, distance: Any) -> None: ...
def check_distance_triangle_inequality(test_obj: Any, distance: Any) -> None: ...

class TestEuclideanDistance(unittest.TestCase):
    euclidean: Any = ...
    def setUp(self) -> None: ...
    def test_triangle_inequality(self) -> None: ...
    def test_symmetry(self) -> None: ...

class TestCosineDistance(unittest.TestCase):
    cosine: Any = ...
    def setUp(self) -> None: ...
    def test_symmetry(self) -> None: ...

class TestManhattanDistance(unittest.TestCase):
    manhattan: Any = ...
    def setUp(self) -> None: ...
    def test_triangle_inequality(self) -> None: ...
    def test_symmetry(self) -> None: ...
