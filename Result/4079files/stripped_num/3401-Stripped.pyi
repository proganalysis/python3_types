# (generated with --quick)

from typing import Any, Dict, List

PipelineParam: Any
PipelineVolume: Any
ResourceOp: Any
V1ObjectMeta: Any
V1PersistentVolumeClaim: Any
V1PersistentVolumeClaimSpec: Any
V1ResourceRequirements: Any
V1TypedLocalObjectReference: Any
VOLUME_MODE_ROM: List[str]
VOLUME_MODE_RWM: List[str]
VOLUME_MODE_RWO: List[str]
match_serialized_pipelineparam: Any
re: module
sanitize_k8s_name: Any

class VolumeOp(Any):
    __doc__: str
    attribute_outputs: Dict[str, str]
    volume: Any
    def __init__(self, resource_name = ..., size = ..., storage_class = ..., modes = ..., annotations = ..., data_source = ..., **kwargs) -> None: ...
    def _validate_memory_string(self, memory_string) -> None: ...
