# (generated with --quick)

from typing import Any, Generator, Tuple

X: Any
Xr: Any
Xs: Any
efs_: Any
extract_features: Any
extract_relevant_features: Any
features_filtered: Any
fts: Any
his: Any
los: Any
rf: Any
timeseries_: Any
x: Any
xdfstd: Any
y: Any
y_: Any
ypred: Any
yr: Any
ys: Any

def batch_getter(x, y) -> Any: ...
def batch_iter(x, y = ..., bptt = ..., evaluation = ...) -> Generator[Any, Any, None]: ...
def get_batch(source, i, bptt = ..., evaluation = ...) -> Any: ...
def seq_batch_iter(x, y = ..., bptt = ..., evaluation = ...) -> Generator[Any, Any, None]: ...
def show_preds(ys, pred) -> None: ...
def split(X, y, ratio = ...) -> Tuple[Any, Any, Any, Any]: ...
def train(model = ..., hidden = ..., brange = ..., batch_getter = ..., optimizer = ..., eval = ...) -> Any: ...
def train_epoch(xt, yt, model = ..., bptt = ..., hidden = ..., optimizer = ..., eval = ...) -> Any: ...
