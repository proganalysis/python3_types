from typing import Any

def recon_err(data: Any, F: Any, W: Any): ...
def get_train_err(htfa: Any, data: Any, F: Any): ...
def get_test_err(htfa: Any, test_weight_data: Any, test_recon_data: Any, test_weight_R: Any, test_recon_R: Any, centers: Any, widths: Any): ...

n_subj: int
comm: Any
rank: Any
size: Any
group_id: Any
n_group: Any
htfa_comm: Any
htfa_rank: Any
htfa_size: Any
data_dir: Any
url: Any
file_name: Any
ret: Any
cmd: Any
retcode: Any
data: Any
R: Any
mapping: Any
n_local_subj: int
all_data: Any
bold: Any
min_K: int
max_K: int
n_K: int
Ks: Any
n_splits: int
test_recon_errs: Any
tmp_test_recon_errs: Any
train_recon_errs: Any
tmp_train_recon_errs: Any
local_size: Any
n_voxel: Any
n_tr: Any
n_dim: Any
test_size: float
rnd_seed_voxel: int
rnd_seed_tr: int
tr_solver: str
nlss_method: str
nlss_loss: str
upper_ratio: float
lower_ratio: float
voxel_ratio: float
tr_ratio: float
max_voxel: int
max_tr: int
max_sample_voxel: Any
max_sample_tr: Any
ss_voxel: Any
voxel_indices: Any
ss_tr: Any
tr_indices: Any
train_voxels: Any
test_voxels: Any
train_trs: Any
test_trs: Any
index: Any
train_voxel_indices = train_voxels[p]
test_voxel_indices = test_voxels[p]
train_tr_indices = train_trs[p]
test_tr_indices = test_trs[p]
train_data: Any
total_test_data: Any
test_weight_data: Any
test_recon_data: Any
test_weight_R: Any
test_recon_R: Any
htfa: Any
subj_idx: Any
start_idx: Any
end_idx: Any
local_posteiror: Any
local_centers: Any
local_widths: Any
unique_R_all: Any
inds_all: Any
train_F: Any
errs: Any
mean_errs: Any
best_idx: Any
