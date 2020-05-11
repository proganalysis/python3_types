# (generated with --quick)

import kernel.common
from typing import Any, MutableMapping, Type, TypeVar

APINotFoundError: Any
DataSource: Any
KernelSource: Type[kernel.common.KernelSource]
NotFoundError: Any
PipelineContext: Any
Platform: Any
Query: Any
Region: Any
ShardStatusDto: Any
VersionListDto: Any
convert_region_to_platform: Any
validate_query: Any

T = TypeVar('T')

class StatusAPI(kernel.common.KernelSource):
    _validate_get_many_status_query: Any
    _validate_get_status_query: Any
    get: Any
    get_many: Any
    get_many_status: Any
    get_status: Any

def _get_default_locale(query: MutableMapping[str, Any], context) -> str: ...
def _get_default_version(query: MutableMapping[str, Any], context) -> str: ...
