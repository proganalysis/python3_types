# (generated with --quick)

import argparse
import pathlib
from typing import Any, Dict, List, Type

AXIS_INVERSION_FOR_RAS: Dict[str, int]
AXIS_PERMUTATION_FOR_RAS: Dict[str, int]
POSSIBLE_AXIS_ORIENTATIONS: List[str]
Path: Type[pathlib.Path]
get_chunk_dtype_transformer: Any
invert_permutation: Any
neuroglancer_scripts: Any
np: module
permute: Any
precomputed_io: Any
readable_count: Any
skimage: Any
sys: module
tqdm: Any
trange: Any

def convert_slices_in_directory(slice_dirs, dest_url, input_orientation = ..., options = ...) -> None: ...
def main(argv = ...) -> int: ...
def parse_command_line(argv) -> argparse.Namespace: ...
def slices_to_raw_chunks(slice_filename_lists, dest_url, input_orientation, options = ...) -> None: ...
