# (generated with --quick)

from typing import Any, Dict

Fs: float
ap: Any
audio: Any
n: int
np: module
pl: Any
polys: Dict[int, nothing]
sys: module
time: module
xcvr: SonarTransciever

class SonarTransciever:
    inBufSize: int
    input_fragment: Any
    outBufSize: int
    output: Any
    period: Any
    def __getitem__(self, sl) -> Any: ...
    def __init__(self, m) -> Any: ...
    def __len__(self) -> Any: ...
    def append(self, sequence) -> None: ...

def mls(n = ...) -> Any: ...
