# (generated with --quick)

import itertools
from typing import Any, Dict, Type

Callback: Any
K: Any
chain: Type[itertools.chain]
matplotlib: Any
numpy: module
os: module
plt: Any
time_formatter: Any
timer: Any

class NotSoChattyLogger(Any):
    _epoch: int
    _metrics: Dict[Any, list]
    _partial_counter: Any
    _print_every: Any
    _start: Any
    _total_counter: Any
    count: Any
    epoch: Any
    start: Any
    def __getitem__(self, item) -> list: ...
    def __init__(self, print_every = ..., start = ..., counter = ..., metrics = ...) -> None: ...
    def on_batch_end(self, batch, logs = ...) -> None: ...

def plot_weights(model, dest_dir, layers = ...) -> None: ...
