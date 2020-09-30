# (generated with --quick)

from typing import Any, Type
import unittest.case

Comment: Any
Http404: Any
Mock: Any
QuerySet: Any
TestCase: Type[unittest.case.TestCase]
_get_comment_pageid: Any

class GetCommentPageIdTestCase(unittest.case.TestCase):
    __doc__: str
    comment_id: int
    mock_comment: Any
    mock_qs_comments: Any
    def check_queryset_parameterized_properly(self) -> None: ...
    def test_raises_http404_when_comment_nonexistent(self) -> None: ...
    def test_returns_pageid_equals_2_with_6_newer_comments(self) -> None: ...
    def test_returns_pageid_equals_3(self) -> None: ...
    def test_returns_pageid_equals_3_with_7_newer_comments(self) -> None: ...
