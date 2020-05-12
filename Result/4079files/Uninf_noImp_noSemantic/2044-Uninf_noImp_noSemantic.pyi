import plotnine as gg
import pandas as pd
from typing import Any, Sequence, Text

NUM_EPISODES: Any
BASE_REGRET: float
TAGS: Any

def score(df: pd.DataFrame) -> float: ...
def plot_learning(df: pd.DataFrame, sweep_vars: Sequence[Text]=...) -> gg.ggplot: ...
def plot_seeds(df_in: pd.DataFrame, sweep_vars: Sequence[Text]=..., colour_var: Text=...) -> gg.ggplot: ...
