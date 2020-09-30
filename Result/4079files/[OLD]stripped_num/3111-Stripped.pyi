# (generated with --quick)

from typing import Any, Optional

Decimal: Any
Field: Any
ParameterBuilder: Any

class NumericParameterBuilder(Any):
    __doc__: str
    def parse_format(self, field) -> Optional[str]: ...
    def parse_type(self, field) -> str: ...
    def supports_field(self, field) -> bool: ...
