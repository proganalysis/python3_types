# (generated with --quick)

from typing import Any

Error: Any
LanguageTool: Any
__version__: Any
argparse: module
locale: module
re: module
sys: module

class RulesAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string = ...) -> None: ...

def get_rules(rules) -> set: ...
def get_text(filename, encoding, ignore) -> str: ...
def main() -> int: ...
def parse_args() -> argparse.Namespace: ...
def print_unicode(text) -> None: ...
