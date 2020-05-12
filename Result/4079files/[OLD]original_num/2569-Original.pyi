# (generated with --quick)

from typing import Any, Dict

BuildProcessStep: Any
ufo: Any

class BuildProcessVolumeAssets(Any):
    __doc__: str
    needed_files_compressed: Dict[str, str]
    needed_files_volume: dict
    def __init__(self, domain) -> None: ...
    def _add_volume_file_reference(self, destination, source) -> None: ...
    def _add_volume_file_reference_raw(self, destination, source) -> None: ...
    def step_0x0(self) -> None: ...
