from typing import Any

n_samples: int
random_state: int
X_varied: Any
y_varied: Any
y_pred: Any
projections: int
proj_method: str

def run_bico_parellel(X: Any) -> None: ...
def run_bico(size: Any, X: Any) -> None: ...

tstart: Any
X_chunks: Any
tend: Any
