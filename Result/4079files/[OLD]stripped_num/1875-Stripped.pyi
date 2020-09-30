# (generated with --quick)

from typing import Any, Dict, List, Type, Union

ClientError: Any
Provider: Any
common: Any
datetime: Type[datetime.datetime]
lambda_tools: Any
logger: Any
timezone: Type[datetime.timezone]

class CZReactorMetrics(Any):
    _TABLE_BASENAME: str
    _TABLE_DEFINITION: Dict[str, Union[Dict[str, int], List[Dict[str, str]]]]
    def __init__(self, namespace = ..., aws = ...) -> None: ...
    def get(self, name, range_key) -> Any: ...
    def write_metric(self, event_count, metric_name, env_id = ...) -> Any: ...
