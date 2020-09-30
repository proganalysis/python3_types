# (generated with --quick)

from typing import Any, Dict, Tuple, Union

ModelTestCase: Any
Place: Any
PlaceFactory: Any

class PlaceTest(Any):
    __doc__: str
    field_tests: Dict[str, Dict[str, Union[int, str]]]
    model: Any
    model_tests: Dict[str, Union[str, Tuple[str]]]
    @classmethod
    def setUpTestData(cls) -> None: ...
    def test_get_absolute_url(self) -> None: ...
    def test_str_is_name(self) -> None: ...
