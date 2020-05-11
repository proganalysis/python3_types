# (generated with --quick)

import itertools
from typing import Any, Type

chain: Type[itertools.chain]

class DefaultConfigMixin:
    _default_config: Any
    config: Any
    def __init__(self, bot, name = ...) -> None: ...
    def configure(self, configuration) -> None: ...
    def get_configuration_template(self) -> Any: ...
