import torch.nn.functional as nn
from typing import Any

class Net(nn.Module):
    conv1: Any = ...
    conv2: Any = ...
    fc1: Any = ...
    fc2: Any = ...
    fc3: Any = ...
    def __init__(self) -> None: ...
    def forward(self, x: Any): ...
    def num_flat_features(self, x: Any): ...
