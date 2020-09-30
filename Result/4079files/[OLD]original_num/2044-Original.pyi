# (generated with --quick)

from typing import Any, Optional, Sequence, Tuple

BASE_REGRET: float
NUM_EPISODES: Any
TAGS: Tuple[str, str]
gg: Any
np: module
pd: Any
plotting: Any
sweep: Any

def plot_learning(df, sweep_vars: Optional[Sequence[str]] = ...) -> Any: ...
def plot_seeds(df_in, sweep_vars: Optional[Sequence[str]] = ..., colour_var: Optional[str] = ...) -> Any: ...
def score(df) -> float: ...
