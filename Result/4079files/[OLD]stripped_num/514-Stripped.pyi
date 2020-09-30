# (generated with --quick)

from typing import Any, Tuple

ClassifyFullySupervised: Any
DATASETS: Any
EasyDict: Any
FLAGS: Any
MultiModel: Any
app: Any
flags: Any
functools: module
os: module
tf: Any
utils: Any

class FSMixup(Any, Any):
    def augment(self, x, l, beta, **kwargs) -> Tuple[Any, Any]: ...
    def model(self, lr, wd, ema, **kwargs) -> Any: ...

def main(argv) -> None: ...
