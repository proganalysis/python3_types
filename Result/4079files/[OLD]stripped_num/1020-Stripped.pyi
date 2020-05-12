# (generated with --quick)

import __future__
from typing import Any

InternalGroupFactory: Any
TestCase: Any
UserFactory: Any
unicode_literals: __future__._Feature

class GroupTest(Any):
    @classmethod
    def setUpTestData(cls) -> None: ...
    def test_group_member_should_have_a_backref(self) -> None: ...
    def test_group_should_contain_a_user(self) -> None: ...
    def test_group_str_and_repr_should_not_fail(self) -> None: ...
