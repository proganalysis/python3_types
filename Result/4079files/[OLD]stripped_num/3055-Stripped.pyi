# (generated with --quick)

from typing import Any, Dict, Tuple, TypeVar

BasePlugin: Any
BaseShortcutPlugin: Any
EQUELPluginException: Any
GenericPlugin: Any

_T1 = TypeVar('_T1')

class AggregationKeywordsPlugin(Any):
    __doc__: str
    description: str
    name: str
    translation: Dict[str, Tuple[str, str]]
    def apply(self, verb, params, parser, ctx) -> None: ...

class AggregationShortcutPlugin(Any):
    __doc__: str
    description: str
    name: str
    translation: Dict[str, Tuple[str, str]]
    def apply(self, prefix, value: _T1, parser, ctx) -> Dict[str, Dict[str, _T1]]: ...

class FilterAggregationPlugin(GenericAggregationPlugin):
    __doc__: str
    description: str
    name: str

class GenericAggregationPlugin(Any):
    __doc__: str
    description: str
    name: str
    def apply(self, verb, *args, **kwargs) -> Any: ...
