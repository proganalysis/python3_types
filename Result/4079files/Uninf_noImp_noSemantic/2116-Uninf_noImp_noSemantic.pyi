from shipmaster.core.plugins import Plugin
from typing import Any

class GraphPlugin(Plugin):
    @classmethod
    def should_load(cls, platform: Any): ...
    @classmethod
    def contribute_to_argparse(cls, parser: Any, commands: Any) -> None: ...

def print_graph(args: Any, config: Any): ...
