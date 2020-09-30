import candle
from sklearn.metrics import accuracy_score as accuracy_score
from typing import Any

file_path: Any
lib_path2: Any
required: Any

class BenchmarkP3B3(candle.Benchmark):
    required: Any = ...
    def set_locals(self) -> None: ...
