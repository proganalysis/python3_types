from impact.tests.api_test_case import APITestCase
from impact.views.algolia_api_key_view import HAS_FINALIST_ROLE_FILTER as HAS_FINALIST_ROLE_FILTER, IS_TEAM_MEMBER_FILTER as IS_TEAM_MEMBER_FILTER
from typing import Any

User: Any

def _create_expert(): ...
def _create_entrepreneur(): ...
def _create_user(factory: Any): ...
def _create_batch_program_and_named_group(status: Any, batch_size: Any): ...

class TestAlgoliaApiKeyView(APITestCase):
    client_class: Any = ...
    user_factory: Any = ...
    url: Any = ...
    def _mentor_directory_url(self): ...
    def _person_directory_url(self): ...
    def test_logged_in_user_with_role_grants_in_ended_programs_gets_403(self) -> None: ...
    def test_logged_in_user_generates_token(self) -> None: ...
    def test_unauthenticated_user_is_denied(self) -> None: ...
    def test_entrepreneur_that_never_had_a_finalist_role_gets_403(self) -> None: ...
    def test_user_with_staff_role_grant_sees_all_mentors(self) -> None: ...
    def test_staff_user_does_not_have_is_active_filter(self) -> None: ...
    def test_finalist_user_filter_includes_is_active_filter(self) -> None: ...
    def test_finalist_user_gets_all_programs_in_program_group(self) -> None: ...
    def test_finalist_user_gets_all_programs_in_past_or_present(self) -> None: ...
    def test_alumni_user_only_sees_mentors_of_alumni_programs(self) -> None: ...
    def test_alumni_user_who_is_also_finalist_sees_mentors_of_both_programs(self) -> None: ...
    def test_superuser_employee_sees_all_mentors(self) -> None: ...
    def test_superuser_employee_sees_people_directory_with_no_filters(self) -> None: ...
    def _create_user_with_role_grant(self, program: Any, user_role_name: Any, user: bool = ...): ...
    def _get_response_data(self, user: Any, directory_url: Any): ...