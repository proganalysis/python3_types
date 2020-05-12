# (generated with --quick)

import requests.packages.urllib3.util.retry
from typing import Any, Dict, List, Pattern, Tuple, Type

AllCompletedFuture: Any
AutoScalingGroup: Any
AzureApi: Any
AzureScaleSet: Any
AzureScaleSetInstance: Any
CompletedFuture: Any
Retry: Type[requests.packages.urllib3.util.retry.Retry]
TransformingFuture: Any
_CLASS_PAT: Pattern[str]
_RETRY_TIME_LIMIT: int
_SCALE_SET_SIZE_LIMIT: int
datetime: Type[datetime.datetime]
http: module
logger: logging.Logger
logging: module
re: module
utils: Any

class AzureBoundedRetry(requests.packages.urllib3.util.retry.Retry):
    BACKOFF_MAX: Any
    __doc__: str
    backoff_factor: Any
    connect: Any
    method_whitelist: Any
    read: Any
    status_forcelist: Any
    total: Any
    def __init__(self, **kwargs) -> None: ...
    @staticmethod
    def from_retry(retry) -> AzureBoundedRetry: ...
    def get_retry_after(self, response) -> Any: ...

class AzureGroups(object):
    client: Any
    resource_groups: Any
    slow_scale_classes: Any
    def __init__(self, resource_groups, slow_scale_classes, client) -> None: ...
    def get_all_groups(self, kube_nodes) -> List[AzureVirtualScaleSet]: ...

class AzureInstance(object):
    id: Any
    instance_type: Any
    launch_time: Any
    provider: str
    tags: Any
    def __init__(self, instance_id, instance_type, launch_time, tags) -> None: ...

class AzureVirtualScaleSet(Any):
    _global_priority: Any
    _id: Tuple[Any, str]
    client: Any
    desired_capacity: Any
    global_priority: Any
    instance_ids: Any
    instance_type: Any
    instances: Dict[Any, AzureInstance]
    is_spot: bool
    max_size: int
    min_size: int
    name: str
    no_schedule_taints: Any
    nodes: Any
    provider: str
    region: Any
    resource_group: Any
    scale_sets: dict
    selectors: Dict[str, Any]
    slow_scale: bool
    tags: Dict[nothing, nothing]
    timeout_reason: Any
    timeout_until: Any
    unschedulable_nodes: Any
    vm_id_to_instance: Dict[Any, Tuple[Any, Any]]
    def __init__(self, region, resource_group, client, instance_type, slow_scale: bool, scale_sets: list, kube_nodes) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def get_azure_instances(self) -> dict_values[AzureInstance]: ...
    def is_timed_out(self) -> bool: ...
    def scale_nodes_in(self, nodes) -> Any: ...
    def set_desired_capacity(self, new_desired_capacity) -> Any: ...
    def terminate_instances(self, vm_ids) -> Any: ...

def _get_azure_class(type_) -> str: ...
