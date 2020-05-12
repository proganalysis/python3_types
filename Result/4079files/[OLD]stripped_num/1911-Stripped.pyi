# (generated with --quick)

from typing import Any, Tuple
import unittest.case

itertools: module
main: Any
os: module
random: module
tempfile: module
unittest: module

class TestMain(unittest.case.TestCase):
    keys: tuple
    plaintexts: tuple
    def test_crypto(self) -> None: ...
    def test_entropy_test(self) -> None: ...

def make_credentials(num_secrets, num_bytes = ...) -> Tuple[Tuple[str, ...], Tuple[str, ...]]: ...
def make_keys(streams, necessary_nibble_grams) -> None: ...
def make_plaintexts(streams, num_bytes = ...) -> Tuple[Tuple[int, ...], ...]: ...
