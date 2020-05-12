# (generated with --quick)

from typing import Any

F: Any
criterion: Any
net: Net
nn: Any
optim: Any
optimizer: Any
torch: Any

class Net(Any):
    conv1: Any
    conv2: Any
    fc1: Any
    fc2: Any
    fc3: Any
    def __init__(self) -> None: ...
    def forward(self, x) -> Any: ...
    def num_flat_features(self, x) -> Any: ...
