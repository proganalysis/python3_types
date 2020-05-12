from caiman.base.rois import extract_binary_masks_blob as extract_binary_masks_blob
from caiman.components_evaluation import estimate_components_quality as estimate_components_quality, evaluate_components as evaluate_components
from caiman.motion_correction import MotionCorrect as MotionCorrect, motion_correction_piecewise as motion_correction_piecewise, tile_and_correct as tile_and_correct
from caiman.tests.comparison import comparison as comparison
from caiman.utils.image_preprocessing_keras import ImageDataGenerator as ImageDataGenerator
from caiman.utils.utils import download_demo as download_demo
from caiman.utils.visualization import plot_contours as plot_contours, view_patches_bar as view_patches_bar
from ipyparallel import Client as Client
from keras.datasets import mnist as mnist
from keras.layers import Dense as Dense, Flatten as Flatten, merge as merge
from keras.layers.core import Lambda as Lambda
from keras.models import Model as Model
from skimage.external.tifffile import TiffFile as TiffFile
from sklearn.model_selection import train_test_split as train_test_split
from typing import Any, Optional

def get_conv(input_shape: Any = ..., filename: Optional[Any] = ...): ...

heatmodel: Any

def locate(data: Any, plot: bool = ..., rectangle: bool = ..., total_pooling: int = ..., prob: float = ...): ...

json_path: str
model_path: str
json_file: Any
loaded_model_json: Any
loaded_model: Any
opt: Any
REGENERATE: bool
total_crops: Any
total_labels: Any
patch_size: int
all_neg_crops: Any
all_pos_crops: Any
all_dubious_crops: Any
gSig: Any
pos: Any
rand_perm: Any
all_masks_gt: Any
labels_gt: Any
num_sampl: int
predictions: Any
fname_new: str
gt_file: Any
base_name: Any
maxT: int
A_gt: Any
dims: Any
C_gt: Any
YrA_gt: Any
f_gt: Any
fname_new = fname_new[]
A_gt_thr: Any
Yr: Any
T: Any
d1: Any
d2: Any
images: Any
Y: Any
m_orig: Any
half_crop: Any
idx_included: Any
idx_excluded: Any
m_res: Any
mean_proj: Any
std_mov: Any
min_mov: Any
full_fov: bool
normalize_median_std: bool
count_start: int
border_size: int
cms_total: Any
all_heatmaps: Any
img_avg: Any
image_no_neurons: Any
image_orig: Any
avg_crops: Any
cm_: Any
ain: Any
