# (generated with --quick)

import collections
from typing import Any, List, Type

ActiveState: Any
EnergyModel: Any
EnergyModelNode: Any
EnergyModelRoot: Any
OrderedDict: Type[collections.OrderedDict]
PowerDomain: Any
a53_cluster_active_states: collections.OrderedDict[int, Any]
a53_cluster_idle_states: collections.OrderedDict[str, int]
a53_cpu_active_states: collections.OrderedDict[int, Any]
a53_cpu_idle_states: collections.OrderedDict[str, int]
a53s: List[int]
a57_cluster_active_states: collections.OrderedDict[int, Any]
a57_cluster_idle_states: collections.OrderedDict[str, int]
a57_cpu_active_states: collections.OrderedDict[int, Any]
a57_cpu_idle_states: collections.OrderedDict[str, int]
a57s: List[int]
nrg_model: Any

def a53_cpu_node(cpu) -> Any: ...
def a57_cpu_node(cpu) -> Any: ...
