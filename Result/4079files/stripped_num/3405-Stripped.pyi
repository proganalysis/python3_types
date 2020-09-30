# (generated with --quick)

from typing import Any

IntegrityError: Any
LocalizedField: Any
LocalizedUniqueSlugField: Any
TestCase: Any
copy: module
forms: Any
get_fake_model: Any
models: Any
settings: Any
slugify: Any

class LocalizedSlugFieldTestCase(Any):
    AutoSlugModel: None
    Model: None
    __doc__: str
    @classmethod
    def setUpClass(cls) -> None: ...
    @staticmethod
    def test_deconstruct() -> None: ...
    @staticmethod
    def test_formfield() -> None: ...
    @classmethod
    def test_populate(cls) -> None: ...
    @classmethod
    def test_populate_callable(cls) -> None: ...
    @staticmethod
    def test_populate_multiple_from_fields() -> None: ...
    @staticmethod
    def test_populate_multiple_from_fields_fk() -> None: ...
    @classmethod
    def test_populate_multiple_languages(cls) -> None: ...
    @classmethod
    def test_unique_slug(cls) -> None: ...
    @classmethod
    def test_unique_slug_unique_max_retries(cls) -> None: ...
    @classmethod
    def test_unique_slug_update(cls) -> None: ...
    @classmethod
    def test_unique_slug_utf(cls) -> None: ...
    @staticmethod
    def test_unique_slug_with_time() -> None: ...
    @classmethod
    def test_uniue_slug_no_change(cls) -> None: ...
