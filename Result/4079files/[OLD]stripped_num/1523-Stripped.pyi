# (generated with --quick)

import collections
from typing import Any, Dict, List, Type

LOG: logging.Logger
OrderedDict: Type[collections.OrderedDict]
compute_cartesian_product: Any
logging: module
operator: module
rewrite_parameter_macros_to_lists: Any

class Experiment(object):
    configuration_space_list: Any
    experiment_configurations: List[ExperimentConfiguration]
    original_definition: Any
    overload_vnf_list: List[nothing]
    pre_configuration: dict
    profile_calculations: List[nothing]
    resource_limitations: Dict[nothing, nothing]
    def __init__(self, definition) -> None: ...
    def _get_experiment_header_space_as_dict(self) -> Dict[str, List[int]]: ...
    def _get_function_resource_space_as_dict(self) -> Dict[str, List[nothing]]: ...
    def _get_mp_space_as_dict(self) -> Dict[str, Any]: ...
    def _get_pre_configuration_as_dict(self) -> dict: ...
    def populate(self) -> None: ...

class ExperimentConfiguration(object):
    RUN_ID: int
    __doc__: str
    experiment: Any
    name: Any
    parameter: Any
    run_id: int
    def __init__(self, experiment, p) -> None: ...

class FunctionExperiment(Experiment):
    configuration_space_list: List[nothing]
    experiment_configurations: List[nothing]
    original_definition: Any
    overload_vnf_list: List[nothing]
    pre_configuration: Dict[nothing, nothing]
    profile_calculations: List[nothing]
    resource_limitations: Dict[nothing, nothing]

class ServiceExperiment(Experiment):
    configuration_space_list: List[nothing]
    experiment_configurations: List[nothing]
    original_definition: Any
    overload_vnf_list: List[nothing]
    pre_configuration: Dict[nothing, nothing]
    profile_calculations: List[nothing]
    resource_limitations: Dict[nothing, nothing]
