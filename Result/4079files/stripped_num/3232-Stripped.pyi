# (generated with --quick)

from typing import Any, Callable

ConfigFile: Any
NetworkedConfigObject: Any

def GenerateConfigFile(load_hook, dump_hook, **kwargs) -> Callable: ...
def GenerateNetworkedConfigFile(load_hook, normal_class_load_hook, normal_class_dump_hook, **kwargs) -> Callable: ...
