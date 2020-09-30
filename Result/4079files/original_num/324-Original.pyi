# (generated with --quick)

import gluon_backend_rep
from typing import Any, Type

Backend: Any
GluonBackendRep: Type[gluon_backend_rep.GluonBackendRep]
GraphProto: Any
TensorProto: Any
helper: Any

class GluonBackend(Any):
    __doc__: str
    @classmethod
    def prepare(cls, model, device = ..., **kwargs) -> gluon_backend_rep.GluonBackendRep: ...
    @classmethod
    def supports_device(cls, device) -> Any: ...

def prepare(model, device = ..., **kwargs) -> gluon_backend_rep.GluonBackendRep: ...
def supports_device(device) -> Any: ...
