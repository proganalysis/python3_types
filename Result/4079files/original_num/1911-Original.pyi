# (generated with --quick)

from typing import Any, BinaryIO, Sequence, Tuple
import unittest.case

itertools: module
main: Any
os: module
random: module
tempfile: module
unittest: module

class TestMain(unittest.case.TestCase):
    keys: Tuple[str, ...]
    plaintexts: Tuple[str, ...]
    def test_crypto(self) -> None: ...
    def test_entropy_test(self) -> None: ...

def make_credentials(num_secrets, num_bytes = ...) -> Tuple[Tuple[str, ...], Tuple[str, ...]]: ...
def make_keys(streams: Sequence[BinaryIO], necessary_nibble_grams: Tuple[Tuple[int, ...]]) -> None: ...
def make_plaintexts(streams: Sequence[BinaryIO], num_bytes = ...) -> Tuple[Tuple[int, ...]]: ...
