# (generated with --quick)

from typing import Any, Callable, Dict, Optional

EventMultiplexer: Any
IMAGES_EXT: str
WrongArgumentsError: Any
argparse: module
args: argparse.Namespace
ge: Any
json: module
logging: module
np: module
operator: module
os: module
parser: argparse.ArgumentParser
plt: Any
re: module
shared_args: Dict[str, Any]
smoothing_technique: Optional[Callable[[Any], Any]]

def create_smoother(f, *args) -> Callable[[Any], Any]: ...
def exp_smoothing_weight_test(value) -> float: ...
def exponential_smoothing(a, weight) -> list: ...
def moving_average(a, n) -> Any: ...
def plot(x, y, x_label: str, scalar, xmax = ..., ymin = ..., ymax = ...) -> None: ...
def plot_gym_monitor_stats(stats_path, xmax = ..., smoothing_function = ..., save_directory = ..., show_plots = ...) -> None: ...
def plot_tasks(data, x_label: str, smoothing_function = ..., xmin = ..., xmax = ..., max_reward = ..., legend = ..., save_directory = ..., show_plots = ...) -> None: ...
def plot_tf_scalar_summaries(summaries_dir, xmin = ..., xmax = ..., smoothing_function = ..., max_reward = ..., x_label = ..., legend = ..., save_directory = ..., show_plots = ...) -> None: ...
def tf_scalar_data(em) -> Dict[Any, Dict[int, Dict[str, list]]]: ...
