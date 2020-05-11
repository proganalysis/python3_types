# (generated with --quick)

import __builtin__
from typing import Any, Dict, List, Tuple

RawAudio: Any
TASK_REPRESENTATION_LEARNING: Any
batchify: Any
np: module
random_segment: Any
random_subsegment: Any

class SpeechSegmentGenerator(object):
    __doc__: str
    batch_size: Any
    batches_per_epoch: int
    data_: Dict[Any, List[Tuple[Any, Any, Any]]]
    duration: Any
    file_labels_: Any
    in_memory: Any
    label_min_duration: Any
    max_duration: Any
    min_duration: Any
    min_duration_: Any
    parallel: Any
    per_epoch: Any
    per_fold: Any
    per_label: Any
    segment_labels_: list
    signature: Dict[str, Dict[str, Tuple[None, Any]]]
    specifications: Dict[str, Any]
    weighted_: bool
    def __call__(self) -> __builtin__.generator: ...
    def __init__(self, feature_extraction, protocol, subset = ..., per_label = ..., per_fold = ..., per_epoch = ..., duration = ..., min_duration = ..., max_duration = ..., label_min_duration = ..., parallel = ..., in_memory = ...) -> None: ...
    def _load_metadata(self, protocol, subset = ...) -> None: ...
    def feature_extraction(self, _1) -> Any: ...
    def generator(self) -> __builtin__.generator[Dict[str, nothing], Any, Any]: ...
