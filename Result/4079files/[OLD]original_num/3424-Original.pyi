# (generated with --quick)

from typing import Any, NoReturn, Optional

argparse: module
magic: Any
np: module
os: module
sys: module

class ArgumentParserError(Exception): ...

class NewArgumentParser(argparse.ArgumentParser):
    def error(self, message) -> NoReturn: ...

def main(args: Optional[list] = ...) -> None: ...
def parse_args(args) -> argparse.Namespace: ...
