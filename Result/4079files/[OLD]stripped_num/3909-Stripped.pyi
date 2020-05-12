# (generated with --quick)

import algorithms
import base_station
import edge_server
from typing import Any, Callable, Dict, Sequence, SupportsFloat, Tuple, Type
import utils

BaseStation: Type[base_station.BaseStation]
DataUtils: Type[utils.DataUtils]
EdgeServer: Type[edge_server.EdgeServer]
KMeansServerPlacer: Type[algorithms.KMeansServerPlacer]
MIPServerPlacer: Type[algorithms.MIPServerPlacer]
RandomServerPlacer: Type[algorithms.RandomServerPlacer]
ServerPlacer: Type[algorithms.ServerPlacer]
TopKServerPlacer: Type[algorithms.TopKServerPlacer]
cplex: Any
csv: module
data: utils.DataUtils
datetime: Type[datetime.datetime]
logging: module
math: module
np: module
os: module
pickle: module
random: module
time: module
vq: Any

def asin(__x: SupportsFloat) -> float: ...
def cos(__x: SupportsFloat) -> float: ...
def memorize(filename) -> Callable[[Any], Any]: ...
def run(data) -> None: ...
def run_problem(problem, n, k) -> Tuple[Any, Any]: ...
def run_with_parameters(problems, n, k) -> Dict[str, Tuple[Any, Any]]: ...
def sqrt(__x: SupportsFloat) -> float: ...
def wraps(wrapped: Callable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable[[Callable], Callable]: ...
