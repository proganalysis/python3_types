# (generated with --quick)

import src.utils
from typing import Any, Dict, List, Optional

PredictionModel: Any
__author__: str
argparse: module
args: Dict[str, Any]
better_exceptions: Any
cadaster_image_filename: Any
cadaster_images_filenames: Any
cv2: Any
evaluate: Any
evaluation_json_file: Any
get_labelled_digits_matrix: Any
get_labelled_parcels_matrix: Any
h_minima: Any
imread: Any
imsave: Any
label: Any
loader: Any
np: module
os: module
parser: argparse.ArgumentParser
pickle: module
tf: Any
tqdm: Any
watershed: Any

def export_geojson(list_polygon_objects: List[src.utils.MyPolygon], export_filename: str, filename_img: str) -> None: ...
def process_cadaster(filename_img: str, segmentation_model_dir: str, transcription_model_dir: str, output_dir: str, plot = ..., evaluation = ...) -> None: ...
def process_watershed_parcel(mask_parcel, text_segmented_probs, cadaster_imgae_gray, transcription_model, plotting_dir: Optional[str] = ...) -> Optional[src.utils.MyPolygon]: ...
