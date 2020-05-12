# (generated with --quick)

from typing import Any, Tuple, Union

get_brainpedia_descr: Any
get_chance_subjects: Any
get_output_dir: Any
gridspec: Any
idx: Any
np: module
os: module
output_dir: Any
pd: Any
plt: Any
re: module
save_dir: str
sns: Any
ticker: Any

def gather_metrics(output_dir, save_dir) -> Tuple[Any, Any]: ...
@overload
def join(path: Union[bytes, _PathLike[bytes]], *paths: Union[bytes, _PathLike[bytes]]) -> bytes: ...
@overload
def join(path: Union[str, _PathLike[str]], *paths: Union[str, _PathLike[str]]) -> str: ...
def plot_accuracies(save_dir) -> None: ...
def plot_mean_accuracies(save_dir) -> None: ...
