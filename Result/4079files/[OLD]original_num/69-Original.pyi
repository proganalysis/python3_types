# (generated with --quick)

from typing import Any, List

Activation: Any
Dense: Any
Dropout: Any
LSTM: Any
RMSprop: Any
Sequential: Any
argparse: module
bmk: module
candle: Any
datetime: module
gParameters: Any
keras: Any
np: module
os: module
pickle: module
sys: module

class LossHistory(Any):
    losses: List[nothing]
    def on_batch_end(self, batch, logs = ...) -> None: ...
    def on_train_begin(self, logs = ...) -> None: ...

def initialize_parameters() -> Any: ...
def run(gParameters) -> None: ...
def sample(preds, temperature = ...) -> Any: ...
