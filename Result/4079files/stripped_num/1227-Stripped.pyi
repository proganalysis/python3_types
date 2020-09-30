# (generated with --quick)

from typing import Any

BaseTestCase: Any
Column: Any
RedisModel: Any
enum: module

class Diner(Any):
    comments: Any
    seat_num: Any
    table_num: Any

class StatusEnum(enum.Enum):
    ACTIVE: str

class TestCompositeKeys(Any):
    def setUp(self) -> None: ...
    def test_partial_composite_key_should_succeed(self) -> None: ...
    def test_valid_composite_key_should_return(self) -> None: ...
