# (generated with --quick)

from typing import Any

Image: module
ImageColor: module
ImageDraw: module
argparse: module
args: argparse.Namespace
json: module
os: module
parser: argparse.ArgumentParser
tqdm: Any
visualizer: MeasureVisualizer

class MeasureVisualizer:
    __doc__: str
    draw_stave_measures: Any
    draw_staves: Any
    draw_system_measures: Any
    def __init__(self, draw_system_measures, draw_stave_measures, draw_staves) -> None: ...
    def _draw_rectangles(self, rectangles, image, color) -> None: ...
    def draw_bounding_boxes_for_all_images_in_directory(self, image_directory, json_annotation_directory) -> None: ...
    def draw_bounding_boxes_into_image(self, image_path, ground_truth_annotations_path) -> None: ...
