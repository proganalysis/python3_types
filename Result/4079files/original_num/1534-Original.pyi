# (generated with --quick)

import benchmark_base
import multiprocessing.pool
from typing import Any, Callable, Iterable, Optional, Tuple, Type

Benchmark: Type[benchmark_base.Benchmark]
N_RUNS: int
N_SAMPLES: int
bz2: module
get_competition_variables_from_df: Any
get_sorted_split: Any
has_concordance: Any
np: module
os: module
pd: Any
random: module
rnd: Any
tempfile: module
time: module

class BenchmarkConcordance(benchmark_base.Benchmark):
    def benchmark(self) -> None: ...
    @staticmethod
    def check_concordance(submission, clusters, ids) -> float: ...
    def gen_more_data(self, train, predict, result) -> Tuple[Any, Any, Any]: ...
    @staticmethod
    def gen_similar_df(df, data_types: list) -> Any: ...
    @staticmethod
    def load_data() -> Tuple[Any, Any, Any]: ...

def Pool(processes: Optional[int] = ..., initializer: Optional[Callable] = ..., initargs: Iterable = ..., maxtasksperchild: Optional[int] = ...) -> multiprocessing.pool.Pool: ...
def main() -> None: ...
