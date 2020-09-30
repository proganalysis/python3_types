import pandas as pd
from matplotlib.axes import Axes as Axes
from typing import Any, Tuple

logger: Any

def plot(stars: pd.DataFrame, *, filename: str=..., figure_size: Tuple[float, float]=..., spacing: float=..., ug_label: str=..., gr_label: str=..., ri_label: str=..., iz_label: str=...) -> None: ...
def draw_subplot(subplot: Axes, xlabel: str, ylabel: str, x: pd.Series, y: pd.Series, color: str=..., point_size: float=..., ratio: float=...) -> None: ...
