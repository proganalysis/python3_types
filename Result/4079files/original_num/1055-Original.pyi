# (generated with --quick)

from typing import Any, Type

log: logging.Logger
logging: module

class crds(Any):
    definition_period: Any
    entity: Any
    label: str
    value_type: Type[float]
    def formula(individu: crds, period) -> Any: ...

class crds_hors_prestations(Any):
    definition_period: Any
    entity: Any
    label: str
    value_type: Type[float]
    def formula(individu: crds_hors_prestations, period) -> Any: ...

class csg(Any):
    definition_period: Any
    entity: Any
    label: str
    value_type: Type[float]
    def formula(individu: csg, period) -> Any: ...

def __getattr__(name) -> Any: ...
