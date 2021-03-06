# (generated with --quick)

from typing import Any, Type
import unittest.case

API_BASE_URL: Any
TOKEN: Any
TestCase: Type[unittest.case.TestCase]
Typeform: Any
requests_mock: Any
urllib: module

class FormsTestCase(unittest.case.TestCase):
    formID: Any
    forms: Any
    def test_forms_correct_params(self) -> None: ...
    def test_forms_create_creates_a_new_form(self) -> None: ...
    def test_forms_create_has_the_correct_path_and_method(self) -> None: ...
    def test_forms_delete_removes_the_correct_uid_form(self) -> None: ...
    def test_forms_get_correct_id(self) -> None: ...
    def test_forms_get_messages_has_the_correct_path_and_method(self) -> None: ...
    def test_forms_get_sets_get_method(self) -> None: ...
    def test_forms_returns_method_and_path(self) -> None: ...
    def test_forms_update_as_patch_updates_a_form(self) -> None: ...
    def test_forms_update_messages_has_the_correct_path_and_method(self) -> None: ...
    def test_forms_update_sets_put_method_in_request_by_default(self) -> None: ...
    def test_forms_update_updates_a_form(self) -> None: ...
