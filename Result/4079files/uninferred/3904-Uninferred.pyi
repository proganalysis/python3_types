from typing import Any

POSSIBLE_AXIS_ORIENTATIONS: Any
AXIS_PERMUTATION_FOR_RAS: Any
AXIS_INVERSION_FOR_RAS: Any

def slices_to_raw_chunks(slice_filename_lists: Any, dest_url: Any, input_orientation: Any, options: Any = ...): ...
def convert_slices_in_directory(slice_dirs: Any, dest_url: Any, input_orientation: str = ..., options: Any = ...) -> None: ...
def parse_command_line(argv: Any): ...
def main(argv: Any = ...): ...
