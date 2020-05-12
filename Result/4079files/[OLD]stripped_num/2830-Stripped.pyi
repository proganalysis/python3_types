# (generated with --quick)

import collections
from typing import Any, Pattern, Type

OrderedDict: Type[collections.OrderedDict]
_add_to_config: bool
_verbose: bool
configparser: module
log: logging.Logger
logging: module
os: module
portage: Any
re: module
re_sym: Pattern[str]

def __getattr__(name) -> Any: ...
def generate_config(kcheck_config, outputfile = ...) -> int: ...
