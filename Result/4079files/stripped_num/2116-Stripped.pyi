# (generated with --quick)

from typing import Any

Platform: Any
Plugin: Any

class GraphPlugin(Any):
    @classmethod
    def contribute_to_argparse(cls, parser, commands) -> None: ...
    @classmethod
    def should_load(cls, platform) -> Any: ...

def print_graph(args, config) -> None: ...
