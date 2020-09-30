# (generated with --quick)

from typing import Any, Callable

argparse: module
args_parser: argparse.ArgumentParser
docker_build_args_parser: argparse.ArgumentParser
docker_entity_inspect_args_parser: argparse.ArgumentParser
docker_inspect_args_parser: argparse.ArgumentParser
docker_run_args_parser: argparse.ArgumentParser
docker_service_create_args_parser: argparse.ArgumentParser
docker_service_update_args_parser: argparse.ArgumentParser
itertools: module
shlex: module
unittest: Any

class Command(object):
    args: Any
    parser: Any
    def __eq__(self, command) -> Any: ...
    def __init__(self, parser, args) -> None: ...
    def __ne__(self, command) -> bool: ...

class FabricioTestCase(Any):
    def command_checker(self, args_parsers = ..., expected_args_set = ..., side_effects = ...) -> Callable: ...

class FailedResult(str):
    failed: bool
    succeeded: bool

class SucceededResult(str):
    failed: bool
    succeeded: bool
