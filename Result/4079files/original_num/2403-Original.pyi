# (generated with --quick)

import __future__
import numpy
from typing import Any, Dict, List, Tuple

absolute_import: __future__._Feature
beam: Any
division: __future__._Feature
math_util: Any
metric_keys: Any
metrics_for_slice_pb2: Any
np: module
print_function: __future__._Feature
six: module
slicer: Any
tf: Any
types: Any

class SerializeMetrics(Any):
    __doc__: str
    _post_export_metrics: list
    def __init__(self, post_export_metrics: list) -> None: ...
    def expand(self, metrics) -> Any: ...

class SerializeMetricsAndPlots(Any):
    __doc__: str
    _post_export_metrics: list
    def __init__(self, post_export_metrics: list) -> None: ...
    def expand(self, metrics_and_plots: Tuple[Any, Any]) -> Tuple[Any, Any]: ...

class SerializePlots(Any):
    __doc__: str
    _post_export_metrics: list
    def __init__(self, post_export_metrics: list) -> None: ...
    def expand(self, plots) -> Any: ...

def _convert_slice_plots(slice_plots: Dict[str, Any], post_export_metrics: list, plot_data: Dict[str, Any]) -> None: ...
def _convert_to_array_value(array: numpy.ndarray) -> Any: ...
def _serialize_metrics(metrics: Tuple[Any, Dict[str, Any]], post_export_metrics: list) -> bytes: ...
def _serialize_plots(plots: Tuple[Any, Dict[str, Any]], post_export_metrics: list) -> bytes: ...
def convert_slice_metrics(slice_metrics: Dict[str, Any], post_export_metrics: list, metrics_for_slice) -> None: ...
def load_and_deserialize_metrics(path: str) -> List[Tuple[Any, Any]]: ...
def load_and_deserialize_plots(path: str) -> List[Tuple[Any, Any]]: ...
