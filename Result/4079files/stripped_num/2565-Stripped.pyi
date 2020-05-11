# (generated with --quick)

from typing import Any

CodeBlock: Any
DatasetEvaluator: Any
FunctionEvaluator: Any
Token: Any
damerau_levenshtein_distance: Any
np: module
pytest: Any
simple_program: Any

class TestDatasetEvaluator:
    def test_dataset_evaluate(self, simple_program) -> None: ...
    def test_default_error_function(self) -> None: ...

class TestFunctionEvaluator:
    def test_function_evaluate(self, simple_program) -> None: ...

def test_levenshtein_distance_seq() -> None: ...
def test_levenshtein_distance_str() -> None: ...
