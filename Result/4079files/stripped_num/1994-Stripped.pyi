# (generated with --quick)

import requests.models
from typing import Any, Callable, Dict, IO, List, Mapping, Optional, Sequence, Union

HTFA: Any
Ks: Any
MPI: Any
R: list
all_data: Any
best_idx: Any
bold: Any
cmd: str
comm: Any
data: list
data_dir: str
e: Any
end_idx: Any
errs: Any
file_name: str
group_id: int
htfa: Any
htfa_comm: Any
htfa_rank: Any
htfa_size: Any
idx: int
index: int
inds_all: Any
local_centers: Any
local_posteiror: Any
local_size: int
local_widths: Any
logging: module
lower_ratio: float
mapping: Dict[str, int]
math: module
max_K: int
max_sample_tr: int
max_sample_voxel: int
max_tr: int
max_voxel: int
mean_errs: Any
mean_squared_error: Any
min_K: int
model_selection: Any
n_K: int
n_dim: Any
n_group: int
n_local_subj: int
n_splits: int
n_subj: int
n_tr: Any
n_voxel: Any
nlss_loss: str
nlss_method: str
np: module
os: module
p: int
rank: Any
requests: module
ret: requests.models.Response
retcode: int
rnd_seed_tr: int
rnd_seed_voxel: int
s: int
scipy: Any
size: Any
ss_tr: Any
ss_voxel: Any
start_idx: Any
stats: Any
subj_idx: int
sys: module
test_index: Any
test_recon_R: list
test_recon_data: list
test_recon_errs: Any
test_size: float
test_tr_indices: Any
test_trs: list
test_voxel_indices: Any
test_voxels: list
test_weight_R: list
test_weight_data: list
tmp_test_recon_errs: Any
tmp_train_recon_errs: Any
total_test_data: list
tr_indices: Any
tr_ratio: float
tr_solver: str
train_F: Any
train_data: list
train_index: Any
train_recon_errs: Any
train_tr_indices: Any
train_trs: list
train_voxel_indices: Any
train_voxels: list
unique_R_all: Any
upper_ratio: float
url: List[str]
voxel_indices: Any
voxel_ratio: float

def call(args: Union[bytes, str, Sequence[Union[_PathLike, bytes, str]]], bufsize: int = ..., executable: Union[_PathLike, bytes, str] = ..., stdin: Optional[Union[int, IO]] = ..., stdout: Optional[Union[int, IO]] = ..., stderr: Optional[Union[int, IO]] = ..., preexec_fn: Callable[[], Any] = ..., close_fds: bool = ..., shell: bool = ..., cwd: Optional[Union[_PathLike, bytes, str]] = ..., env: Optional[Mapping[Union[bytes, str], Union[bytes, str]]] = ..., universal_newlines: bool = ..., startupinfo = ..., creationflags: int = ..., restore_signals: bool = ..., start_new_session: bool = ..., pass_fds = ..., timeout: Optional[float] = ...) -> int: ...
def get_test_err(htfa, test_weight_data, test_recon_data, test_weight_R, test_recon_R, centers, widths) -> float: ...
def get_train_err(htfa, data, F) -> float: ...
def recon_err(data, F, W) -> float: ...
