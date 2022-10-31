import enum
from .base import BaseTestCase
from subconscious.model import RedisModel
from typing import Any

class StatusEnum(enum.Enum):
    ACTIVE: str = ...

class Diner(RedisModel):
    table_num: Any = ...
    seat_num: Any = ...
    comments: Any = ...

class TestGetObectOrNone(BaseTestCase):
    def setUp(self) -> None: ...
    def test_get_object_or_none(self) -> None: ...