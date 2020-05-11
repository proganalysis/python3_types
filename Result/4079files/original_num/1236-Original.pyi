# (generated with --quick)

from typing import Any, List, Optional, Tuple

Colormap: Any
PECULIAR_SOLAR_VELOCITY_U: Any
PECULIAR_SOLAR_VELOCITY_V: Any
PECULIAR_SOLAR_VELOCITY_W: Any
cm: Any
logger: logging.Logger
logging: module
matplotlib: Any
np: module
pd: Any
plt: Any

def colormap_by_name(name: str, *, under: Optional[str] = ...) -> Any: ...
def draw_plot(*, xlabel: str, ylabel: str, xdata: List[float], ydata: List[float], filename: str, figure_size: Tuple[float, float] = ..., ratio: float = ..., spacing: float = ..., figure_grid_height_ratios: Optional[List[float]] = ..., bins_count: int = ..., vmin: float = ...) -> None: ...
def plot(stars, *, axes: str, uv_filename: str = ..., uw_filename: str = ..., vw_filename: str = ..., u_label: str = ..., v_label: str = ..., w_label: str = ...) -> None: ...
