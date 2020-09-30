from fully_supervised.lib.train import ClassifyFullySupervised
from libml.models import MultiModel
from typing import Any

FLAGS: Any

class FSMixup(ClassifyFullySupervised, MultiModel):
    def augment(self, x: Any, l: Any, beta: Any, **kwargs: Any): ...
    def model(self, lr: Any, wd: Any, ema: Any, **kwargs: Any): ...

def main(argv: Any) -> None: ...
