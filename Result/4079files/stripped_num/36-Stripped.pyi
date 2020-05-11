# (generated with --quick)

from typing import Any

CleanModelFactory: Any
FuzzyText: Any
Item: Any
Material: Any
TestCase: Any
ValidationError: Any

class FixedItemFactory(Any):
    Meta: type
    name: str

class ItemFactory(Any):
    Meta: type
    name: Any

class MaterialFactory(Any):
    Meta: type

class SimpleItemFactory(Any):
    Meta: type

class SimpleItemFactoryGOC(Any):
    Meta: type

class TestFixedItemFactory(Any):
    def test_duplicate(self) -> None: ...
    def test_happy_build_no_name(self) -> None: ...
    def test_make_single(self) -> None: ...

class TestItemFactory(Any):
    def test_make_multi(self) -> None: ...
    def test_make_single(self) -> None: ...

class TestMaterialFactory(Any):
    def test_error_all(self) -> None: ...
    def test_make_single(self) -> None: ...

class TestSimpleItemFactory(Any):
    __doc__: str
    def test_happy(self) -> None: ...
    def test_happy_build(self) -> None: ...
    def test_happy_build_not_clean(self) -> None: ...
    def test_happy_build_save(self) -> None: ...
    def test_missing_name(self) -> None: ...
    def test_name_too_long(self) -> None: ...
    def test_no_get_or_create(self) -> None: ...
