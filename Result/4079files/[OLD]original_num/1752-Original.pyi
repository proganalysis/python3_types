# (generated with --quick)

from typing import Any, Callable, Dict, Hashable, NoReturn, Optional, Tuple, TypeVar

Context: Any
DEFAULT: Any
DELTAS_ANNOTATION: str
FixtureRequest: Any
KUBE_CONFIG: Any
KUBE_SAFETY_CHECK_CONFIG_KEY: str
LABEL_ZONE: Dict[str, str]
LABEL_ZONE_KEY: str
LABEL_ZONE_VALUE: str
MagicMock: Any
Mock: Any
_logger: Any
contextlib: module
errors: Any
fx_annotation_deltas: Any
fx_kube_config: Any
fx_mock_context_kube_client: Any
fx_mock_context_kube_config: Any
fx_volume_zone_label: Any
kube: Any
mock: module
mock_kube: Callable[..., contextlib._GeneratorContextManager]
pykube: Any
pytest: Any
structlog: Any

_T0 = TypeVar('_T0')

class MockKubernetes(Any):
    ResourceKey: type
    patch: Any
    resource_map: dict
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def add_resource(cls, resource, overwrite = ...) -> None: ...
    def get_or_none(self, resource_type: type, name: str, namespace: Optional[str] = ...) -> Any: ...
    @classmethod
    def make_key(cls, resource_type: type, name: str, namespace = ...) -> Any: ...
    @classmethod
    def resource_key(cls, resource) -> Hashable: ...
    def watch(self, resource_type: type) -> NoReturn: ...

def make_resource(resource_type: type, name, namespace = ..., labels = ..., annotations = ..., spec = ...) -> Any: ...
def make_volume_and_claim(ctx, volume_name = ..., claim_name = ..., volume_annotations = ..., claim_annotations = ..., claim_namespace = ..., volume_zone_label = ...) -> Tuple[Any, Any]: ...
def spec_gce_persistent_disk(pd_name: _T0) -> Dict[str, Dict[str, _T0]]: ...
