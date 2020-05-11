# (generated with --quick)

from typing import Any
import unittest.mock

api: Any
db: Any
errors: Any
inject_config: Any
model: Any
patch: unittest.mock._patcher
pytest: Any
snapshots: Any
tags: Any
test_trying_to_omit_mandatory_field: Any

def test_merging(user_factory, tag_factory, context_factory, post_factory) -> None: ...
def test_trying_to_merge_non_existing(user_factory, tag_factory, context_factory) -> None: ...
def test_trying_to_merge_without_privileges(user_factory, tag_factory, context_factory) -> None: ...
