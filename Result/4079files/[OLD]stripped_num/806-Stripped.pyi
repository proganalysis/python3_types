# (generated with --quick)

from typing import Any
import unittest.case

csr_matrix: Any
io: Any
load_dexter: Any
np: module
random_sparse_matrix: Any
tempfile: module
unittest: module

class TestIO(unittest.case.TestCase):
    density: float
    dist: Any
    lab: Any
    matrix_n: int
    similarity: Any
    vect: Any
    def test_check_dist_vs_classes(self) -> None: ...
    def test_check_dist_vs_vectors(self) -> None: ...
    def test_check_shape(self) -> None: ...
    def test_check_valid_metric(self) -> None: ...
    def test_load_dexter(self) -> None: ...
    def test_random_sparse_similarity_matrix_correct_size(self) -> None: ...
    def test_random_sparse_similarity_matrix_correct_type(self) -> None: ...
    def test_random_sparse_similarity_matrix_density(self) -> None: ...
    def test_random_sparse_similarity_matrix_max_one(self) -> None: ...
    def test_random_sparse_similarity_matrix_min_zero(self) -> None: ...
    def test_random_sparse_similarity_matrix_quadratic_form(self) -> None: ...
    def test_random_sparse_similarity_matrix_self_similarity_one(self) -> None: ...
    def test_random_sparse_similarity_matrix_symmetric(self) -> None: ...
    def test_save_and_load_csr_matrix(self) -> None: ...
