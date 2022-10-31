from autoscaler.autoscaling_groups import AutoScalingGroup
from autoscaler.azure_api import AzureApi as AzureApi, AzureScaleSet as AzureScaleSet, AzureScaleSetInstance as AzureScaleSetInstance
from requests.packages.urllib3 import Retry
from typing import Any, List

logger: Any
_RETRY_TIME_LIMIT: int

class AzureBoundedRetry(Retry):
    def __init__(self, **kwargs: Any) -> None: ...
    @staticmethod
    def from_retry(retry: Any): ...
    def get_retry_after(self, response: Any): ...

class AzureGroups:
    resource_groups: Any = ...
    slow_scale_classes: Any = ...
    client: Any = ...
    def __init__(self, resource_groups: Any, slow_scale_classes: Any, client: AzureApi) -> None: ...
    def get_all_groups(self, kube_nodes: Any): ...

_CLASS_PAT: Any

def _get_azure_class(type_: Any): ...

_SCALE_SET_SIZE_LIMIT: int

class AzureVirtualScaleSet(AutoScalingGroup):
    provider: str = ...
    client: Any = ...
    instance_type: Any = ...
    tags: Any = ...
    name: Any = ...
    scale_sets: Any = ...
    desired_capacity: Any = ...
    region: Any = ...
    resource_group: Any = ...
    selectors: Any = ...
    slow_scale: Any = ...
    min_size: int = ...
    max_size: int = ...
    is_spot: bool = ...
    vm_id_to_instance: Any = ...
    instances: Any = ...
    timeout_until: Any = ...
    timeout_reason: Any = ...
    _global_priority: Any = ...
    no_schedule_taints: Any = ...
    nodes: Any = ...
    unschedulable_nodes: Any = ...
    _id: Any = ...
    def __init__(self, region: Any, resource_group: Any, client: AzureApi, instance_type: Any, slow_scale: bool, scale_sets: List[AzureScaleSet], kube_nodes: Any) -> None: ...
    def is_timed_out(self): ...
    @property
    def global_priority(self): ...
    def get_azure_instances(self): ...
    @property
    def instance_ids(self): ...
    def set_desired_capacity(self, new_desired_capacity: Any): ...
    def terminate_instances(self, vm_ids: Any): ...
    def scale_nodes_in(self, nodes: Any): ...
    def __str__(self): ...
    def __repr__(self): ...

class AzureInstance:
    provider: str = ...
    id: Any = ...
    instance_type: Any = ...
    launch_time: Any = ...
    tags: Any = ...
    def __init__(self, instance_id: Any, instance_type: Any, launch_time: Any, tags: Any) -> None: ...
    def __str__(self): ...
    def __repr__(self): ...