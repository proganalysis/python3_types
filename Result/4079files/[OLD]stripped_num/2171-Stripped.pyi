# (generated with --quick)

import collections
from typing import Any, List, Type

default_impls: List[str]
defaultdict: Type[collections.defaultdict]
husl: Any
imageio: Any
img: Any
impls: Any
iters: Any
np: module
nphusl: Any
pytest: Any
sys: module
tabulate: module
timeit: module

class CachedImg:
    hsl: Any
    path: Any
    rgb: Any

def _test_all(fn, img, env, impls, iters) -> None: ...
def test_perf_husl_to_rgb(impls, iters, img) -> None: ...
def test_perf_rgb_to_hue(impls, iters, img) -> None: ...
def test_perf_rgb_to_husl(impls, iters, img) -> None: ...
def test_perf_rgb_to_husl_one_triplet(impls, iters) -> None: ...
