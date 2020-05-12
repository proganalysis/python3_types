# (generated with --quick)

import argparse
import ssd300
from typing import Any, Type

ArgumentParser: Type[argparse.ArgumentParser]
COCODetection: Any
DataLoader: Any
DefaultBoxes: Any
Encoder: Any
Image: module
Pipeline: Any
SSD300: Type[ssd300.SSD300]
SSDTransformer: Any
dboxes300_coco: Any
io: module
json: module
load_checkpoint: Any
np: module
ops: Any
os: module
patches: Any
plt: Any
random: module
time: module
torch: Any
transforms: Any
types: Any

def main() -> None: ...
def parse_args() -> argparse.Namespace: ...
def print_image(image, model, encoder, inv_map, name_map, category_id_to_color, threshold) -> None: ...
