# (generated with --quick)

import io
from typing import Any, Tuple, Type

BytesIO: Type[io.BytesIO]
Image: module
argparse: module
caffe: Any
np: module
sys: module

def caffe_preprocess_and_compute(pimg, caffe_transformer = ..., caffe_net = ..., output_layers = ...) -> Any: ...
def load_model(model_def = ..., pretrained_model = ...) -> Tuple[Any, Any]: ...
def main(argv) -> None: ...
def resize_image(img_data, size = ...) -> bytearray: ...
