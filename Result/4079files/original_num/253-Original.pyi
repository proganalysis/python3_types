# (generated with --quick)

import collections
from typing import Any, Type

Config: Any
LightbusPlugin: Any
MetricsPlugin: Any
OrderedDict: Type[collections.OrderedDict]
PluginRegistry: Any
StatePlugin: Any
pytest: Any
pytestmark: Any
test_execute_hook: Any

def test_autoload_plugins(plugin_registry) -> None: ...
def test_is_plugin_loaded(plugin_registry) -> None: ...
def test_manually_set_plugins(plugin_registry) -> None: ...
def test_plugin_config() -> None: ...
