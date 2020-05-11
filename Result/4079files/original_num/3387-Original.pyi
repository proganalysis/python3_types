# (generated with --quick)

from typing import Any

base: Any
db: Any
logging: module
models: Any
sqlalchemy: Any

class ReleaseCherrypickCountMetric(Any):
    UNIT: str
    __doc__: str
    def _compute_value(self) -> float: ...
    def _format_value(self, num_cherrypicks: float) -> str: ...
    def _score_value(self, num_cherrypicks: float) -> Any: ...
