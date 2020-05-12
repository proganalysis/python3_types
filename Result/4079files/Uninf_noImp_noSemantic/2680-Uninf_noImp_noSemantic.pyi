import numpy as np
from scipy import sparse
from typing import Any

LOG: Any
nn: int
data: Any

def from_matlab(key: str) -> sparse.csr_matrix: ...

W: Any
L: Any
pct: Any

def comp(): ...

target: Any
osc: Any
osc_knl: Any
osc_fn: Any
cfun: Any
net: Any
net_knl: Any
net_fn: Any
scm: Any
scm_knl: Any
scm_fn: Any
L_data: np.ndarray
D: Any
Dmax: Any
nnode: Any
next: Any
state: Any
drift: Any
input: Any
param: Any
diffs: Any
obsrv: Any

def step(n_step: int = ...) -> None: ...
