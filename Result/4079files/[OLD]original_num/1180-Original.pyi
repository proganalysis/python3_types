# (generated with --quick)

from typing import Any, TypeVar
import unittest.case

BatchIterator: Any
CV: Any
Chunks: Any
Data: Any
HDF5: Any
Metadata: Any
PTsne: Any
TMP_PATH: Any
TSNe: Any
check_or_create_path_dir: Any
np: module
os: module
unittest: module

_T0 = TypeVar('_T0')

class TestUnsupervicedModel(unittest.case.TestCase):
    x: Any
    def test_P(self) -> None: ...
    def test_parametric_tsne(self) -> None: ...
    def train(self, ae: _T0, model_params = ...) -> _T0: ...
