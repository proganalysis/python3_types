# (generated with --quick)

from typing import Any, List

DatasetPlugin: Any
build_transforms: Any
path: module
register_data: Any
torchvision: Any
transforms: Any

class ImageFolder(Any):
    sources: List[str]
    def handle(self, source, copy_to_local = ..., normalize = ..., tanh_normalization = ..., **transform_args) -> None: ...
