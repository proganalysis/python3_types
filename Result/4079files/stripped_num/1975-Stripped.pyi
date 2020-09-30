# (generated with --quick)

from typing import Any
import unittest.case

EXAMPLES: Any
MODES: Any
PATHS: Any
_LOG: logging.Logger
ast: module
astunparse: Any
logging: module
typed_ast: module
typed_astunparse: Any
unittest: module

class DumpTests(unittest.case.TestCase):
    __doc__: str
    maxDiff: None
    def test_dump_examples(self) -> None: ...
    def test_dump_files_comparison(self) -> None: ...
    def test_many_dump_roundtrips(self) -> None: ...

def _postprocess_dump(tested_typed_dump) -> str: ...
