from collections import defaultdict as defaultdict
from typing import Any

default_impls: Any

def impls(request: Any): ...
def iters(request: Any): ...

class CachedImg:
    rgb: Any = ...
    hsl: Any = ...
    path: Any = ...

def img(request: Any): ...
def test_perf_husl_to_rgb(impls: Any, iters: Any, img: Any) -> None: ...
def test_perf_rgb_to_husl(impls: Any, iters: Any, img: Any) -> None: ...
def test_perf_rgb_to_husl_one_triplet(impls: Any, iters: Any) -> None: ...
def test_perf_rgb_to_hue(impls: Any, iters: Any, img: Any) -> None: ...
def _test_all(fn: Any, img: Any, env: Any, impls: Any, iters: Any): ...
