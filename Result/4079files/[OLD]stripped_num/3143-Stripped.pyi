# (generated with --quick)

import collections
from typing import Any, Type
import yaml.dumper
import yaml.loader

OrderedDict: Type[collections.OrderedDict]
yaml: module

class MachinaeDumper(yaml.dumper.Dumper): ...

class MachinaeLoader(yaml.loader.SafeLoader):
    def construct_mapping(self, node) -> collections.OrderedDict: ...

def dump(*args, **kwargs) -> None: ...
def listsites(conf) -> str: ...
def safe_load(*args, **kwargs) -> Any: ...
