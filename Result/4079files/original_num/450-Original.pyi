# (generated with --quick)

import numpy
from typing import Any, List

IECore: Any
IENetwork: Any
cv2: Any
np: module

class tiny_yolo_processor:
    DETECTION_THRESHOLD: float
    EXAMPLES_BASE_DIR: str
    LABELS_FILE_NAME: str
    MAX_IOU: float
    _filtered_objs: List[list]
    _ie: Any
    _probability_threshold: float
    _ty_c: Any
    _ty_exec_net: Any
    _ty_input_blob: Any
    _ty_input_shape: Any
    _ty_labels: List[str]
    _ty_n: Any
    _ty_net: Any
    _ty_output: Any
    _ty_output_blob: Any
    _ty_output_shape: Any
    ty_h: Any
    ty_w: Any
    def __init__(self, ty_ir: str, ie, device: str) -> None: ...
    def _boxes_to_pixel_units(self, box_list, image_width, image_height, grid_size) -> None: ...
    def _filter_objects(self, input_image_width, input_image_height) -> List[list]: ...
    def _get_duplicate_box_mask(self, box_list) -> numpy.ndarray: ...
    def _get_intersection_over_union(self, box_1, box_2) -> Any: ...
    def tiny_yolo_inference(self, input_image) -> List[list]: ...
