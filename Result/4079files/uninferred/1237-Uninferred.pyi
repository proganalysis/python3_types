import numpy as _lpy_np
from tvb_hpc import model as model
from typing import Any, List

LOG: Any

def make_data(): ...
def prep_arrays(nsims: Any, nnode: int) -> List[_lpy_np.ndarray]: ...
def run_all(args: Any): ...
def run() -> None: ...
