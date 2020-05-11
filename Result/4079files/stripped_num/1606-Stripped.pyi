# (generated with --quick)

from typing import Any, Dict

EI: Any
EnvPrior: Any
FabolasGPMCMC: Any
InformationGainPerUnitCost: Any
MarginalizationGPMCMC: Any
RandomSampling: Any
george: Any
init_latin_hypercube_sampling: Any
json: module
logger: logging.Logger
logging: module
np: module
os: module
projected_incumbent_estimation: Any
time: module

def fabolas(objective_function, lower, upper, s_min, s_max, n_init = ..., num_iterations = ..., subsets = ..., inc_estimation = ..., burnin = ..., chain_length = ..., n_hypers = ..., output_path = ..., rng = ...) -> Dict[str, Any]: ...
def retransform(s_transform, s_min, s_max) -> int: ...
def transform(s, s_min, s_max) -> Any: ...
