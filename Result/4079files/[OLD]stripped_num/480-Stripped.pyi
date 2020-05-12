# (generated with --quick)

from typing import Any
import unittest.case

Bar: Any
Baz: Any
C1: Any
C2: Any
C3: Any
Cat: Any
Dog: Any
EchoDirectoryFormat: Any
EchoFormat: Any
Foo: Any
FormatRecord: Any
FourInts: Any
FourIntsDirectoryFormat: Any
IntSequence1: Any
IntSequence2: Any
IntSequenceDirectoryFormat: Any
IntSequenceFormat: Any
IntSequenceFormatV2: Any
IntSequenceV2DirectoryFormat: Any
Kennel: Any
Mapping: Any
MappingDirectoryFormat: Any
RedundantSingleIntDirectoryFormat: Any
SemanticTypeRecord: Any
SingleInt: Any
get_dummy_plugin: Any
qiime2: Any
unittest: module

class TestPluginManager(unittest.case.TestCase):
    plugin: Any
    pm: Any
    def test_importable_formats(self) -> None: ...
    def test_importable_formats_excludes_unimportables(self) -> None: ...
    def test_importable_types(self) -> None: ...
    def test_plugins(self) -> None: ...
    def test_semantic_types(self) -> None: ...
