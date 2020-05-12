from .internal import ContextMethodDecorator
from contextlib import ContextDecorator
from typing import Any

tf: Any

class LogFileWriter(ContextDecorator, ContextMethodDecorator):
    experiment: Any = ...
    def __init__(self, experiment: Any): ...
