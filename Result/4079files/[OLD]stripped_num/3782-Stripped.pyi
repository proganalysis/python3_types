# (generated with --quick)

from typing import Any
import unittest.case

Clip: Any
Extension: Any
Formatter: Any
InlineFormat: Any
STATIC_OBJECT: StaticObject
Settings: Any
SinglePixelFrame: Any
TestPNGOutput: Any
Yuuno: Any
YuunoIPythonEnvironment: Any
base64: module
globalipapp: Any
inline_resolved: Any
load_ipython_extension: Any
unittest: module
unload_ipython_extension: Any

class StaticObject(object): ...

class TestClip(Any):
    __getitem__: Any
    def __len__(self) -> int: ...

class TestClipExtension(Any):
    def initialize(self) -> None: ...
    @classmethod
    def is_supported(cls) -> bool: ...

class TestFormatter(unittest.case.TestCase):
    loaded: bool
    shell: Any
    def test_001_formatter_correct_image(self) -> None: ...
    def test_002_formatter_lookup_success(self) -> None: ...
    def test_003_formatter_unload_success(self) -> None: ...
