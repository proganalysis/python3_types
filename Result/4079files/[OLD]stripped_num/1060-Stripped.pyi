# (generated with --quick)

from typing import Any, Mapping

DataArray: Any
Field: Any
overrides: Any

class MetadataField(Any, Mapping[str, Any]):
    __doc__: str
    as_tensor: Any
    batch_tensors: Any
    empty_field: Any
    get_padding_lengths: Any
    metadata: Any
    def __getitem__(self, key) -> Any: ...
    def __init__(self, metadata) -> None: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> int: ...
