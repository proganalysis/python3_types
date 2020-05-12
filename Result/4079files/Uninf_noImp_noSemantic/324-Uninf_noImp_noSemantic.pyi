from onnx import TensorProto as TensorProto, helper as helper
from onnx.backend.base import Backend
from typing import Any

class GluonBackend(Backend):
    @classmethod
    def prepare(cls, model: Any, device: str = ..., **kwargs: Any): ...
    @classmethod
    def supports_device(cls, device: Any): ...

prepare: Any
supports_device: Any
