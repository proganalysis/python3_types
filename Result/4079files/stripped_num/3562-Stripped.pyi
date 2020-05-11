# (generated with --quick)

from typing import Any, Dict, List, Tuple, TypeVar, Union

BadArguments: Any
Provider: Any
ProviderResource: Any
ResourceError: Any
Response: Any
requests: Any

_T0 = TypeVar('_T0')

class Statuspage(StatuspageMixin, Any):
    _Statuspage__component_ids: Dict[str, Union[str, Dict[str, str]]]
    __doc__: str
    _required: Dict[str, List[str]]
    _resources: Dict[str, StatuspageComponents]
    _schema: Dict[str, Union[bool, str, Dict[str, Union[Dict[str, Union[str, Dict[str, str], List[str]]], List[str]]]]]
    incidents_url: str
    realtime_statuses: List[str]
    scheduled_statuses: List[str]
    def _prepare_data(self, data) -> Dict[str, Any]: ...
    def _send_notification(self, data) -> Any: ...
    def _validate_data_dependencies(self, data: _T0) -> _T0: ...

class StatuspageComponents(StatuspageMixin, Any):
    __doc__: str
    _required: Dict[str, List[str]]
    _schema: Dict[str, Union[bool, str, Dict[str, Dict[str, str]]]]
    components_url: str
    resource_name: str
    def _get_resource(self, data) -> Any: ...

class StatuspageMixin:
    __doc__: str
    base_url: str
    name: str
    path_to_errors: Tuple[str]
    site_url: str
