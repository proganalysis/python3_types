# (generated with --quick)

from typing import Any, Dict, List, Tuple, Union

NominationFactory: Any
Project: Any
ProjectFactory: Any
ResourceFactory: Any
TestCase: Any
UserFactory: Any
pytest: Any
reverse: Any

class ProjectDetailViewTests(Any):
    admin_user: Any
    blacklisted_user: Any
    fields: List[str]
    nominator: Any
    outside_user: Any
    templates: List[str]
    test_absolute_url_method: Any
    test_edit_project_link: Any
    test_included_fields: Any
    test_instance: Any
    test_new_nomination_link: Any
    test_response: Any
    test_update_link: Any
    user_nominations: Dict[str, Union[str, Tuple[str, ...]]]
    def setUp(self) -> None: ...

class ProjectIndexViewTests(Any):
    response: Any
    test_instances: list
    test_links_to_all_projects: Any
    def setUp(self) -> None: ...

class ProjectUpdateViewTests(Any):
    admin_user: Any
    project: Any
    response: Any
    test_included_fields: Any
    test_load: Any
    test_no_edit_if_not_admin: Any
    url: Any
    def setUp(self) -> None: ...

class TestProjectCreateView:
    test_anonymous_cant_create_project: Any
    test_user_creates_project: Any

class TestProjectIndexView:
    test_new_project_link: Any
    test_project_table: Any
