# (generated with --quick)

import lib.ip
import lib.scanner
from typing import Any, Type

IPV4Network: Type[lib.ip.IPV4Network]
Scanner: Type[lib.scanner.Scanner]
SingleTable: Any
argparse: module
concurrent: module
time: module

def build_parser() -> argparse.ArgumentParser: ...
def ip2int(row) -> int: ...
def main() -> None: ...
def tableprinter(data) -> None: ...
