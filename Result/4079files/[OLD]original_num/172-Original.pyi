# (generated with --quick)

import multiprocessing.pool
import numpy
from typing import Any, Callable, Iterable, List, Optional, Tuple

ConsoleLogging: Any
R_bins: Any
R_bins_np: Any
RawArray: Any
StratifiedShuffleSplit: Any
X: Any
X_bins: Any
X_bins_np: Any
Y: Any
Y_bins: Any
Y_bins_np: Any
__all__: List[str]
cdist: Any
check_vector_matrix_shape_fits_labels: Any
ctypes: module
d: Any
histograms: list
kth: Any
mp: Any
mp_np: Any
n_bins: Any
n_x: Any
n_y: Any
np: module
p: Any
pairwise_distances: Any
pdist: Any
squareform: Any

def Pool(processes: Optional[int] = ..., initializer: Optional[Callable] = ..., initargs: Iterable = ..., maxtasksperchild: Optional[int] = ...) -> multiprocessing.pool.Pool: ...
def _mp_calc_histograms(i) -> Any: ...
def _mp_calc_histograms_n_bins(i) -> Any: ...
def _mp_calc_mp_dissim(x) -> None: ...
def _mp_create_r_bins(i) -> None: ...
def _mp_estimate_r(i) -> None: ...
def _mp_find_bin_edges(i) -> Any: ...
def _mp_load_shared_Y(Y_, n_bins_) -> None: ...
def _mp_load_shared_data(X_, Y_, p_, n_bins_, R_bins_, R_bins_np_, X_bins_, X_bins_np_, Y_bins_, Y_bins_np_, mp_, mp_np_) -> None: ...
def cosine_distance(X) -> Any: ...
def cpu_count() -> int: ...
def euclidean_distance(X) -> Any: ...
def lp_norm(X: numpy.ndarray, Y: Optional[numpy.ndarray] = ..., p: Optional[float] = ..., n_jobs: int = ...) -> Any: ...
def mp_dissim(X: numpy.ndarray, Y: Optional[numpy.ndarray] = ..., p: float = ..., n_bins: int = ..., bin_size: str = ..., n_jobs: int = ..., verbose: int = ...) -> Any: ...
def sample_distance(X, y, sample_size, metric = ..., strategy = ..., random_state = ...) -> Tuple[Any, Any]: ...
