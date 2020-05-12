# (generated with --quick)

from typing import Any

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

def colormap_by_name(name, *, under = ...) -> Any: ...
def draw_plot(*, xlabel, ylabel, xdata, ydata, filename, figure_size = ..., ratio = ..., spacing = ..., figure_grid_height_ratios = ..., bins_count = ..., vmin = ...) -> None: ...
def plot(stars, *, axes, uv_filename = ..., uw_filename = ..., vw_filename = ..., u_label = ..., v_label = ..., w_label = ...) -> None: ...
