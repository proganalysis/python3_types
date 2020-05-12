from gitlabform.gitlab.core import GitLabCore
from typing import Any

class GitLabProjects(GitLabCore):
    def get_all_projects(self): ...
    def post_deploy_key(self, project_and_group_name: Any, deploy_key: Any) -> None: ...
    def get_deploy_keys(self, project_and_group_name: Any): ...
    def get_deploy_key(self, project_and_group_name: Any, id: Any): ...
    def post_secret_variable(self, project_and_group_name: Any, secret_variable: Any) -> None: ...
    def put_secret_variable(self, project_and_group_name: Any, secret_variable: Any) -> None: ...
    def get_secret_variable(self, project_and_group_name: Any, secret_variable_key: Any): ...
    def get_secret_variables(self, project_and_group_name: Any): ...
    def get_project_settings(self, project_and_group_name: Any): ...
    def put_project_settings(self, project_and_group_name: Any, project_settings: Any) -> None: ...
    def get_project_push_rules(self, project_and_group_name: Any): ...
    def put_project_push_rules(self, project_and_group_name: Any, push_rules: Any) -> None: ...
    def get_hook_id(self, project_and_group_name: Any, url: Any): ...
    def delete_hook(self, project_and_group_name: Any, hook_id: Any) -> None: ...
    def put_hook(self, project_and_group_name: Any, hook_id: Any, url: Any, data: Any) -> None: ...
    def post_hook(self, project_and_group_name: Any, url: Any, data: Any) -> None: ...
    def post_approvals(self, project_and_group_name: Any, data: Any) -> None: ...
    def put_approvers(self, project_and_group_name: Any, approvers: Any, approver_groups: Any) -> None: ...
    def share_with_group(self, project_and_group_name: Any, group_name: Any, group_access: Any, expires_at: Any): ...
    def unshare_with_group(self, project_and_group_name: Any, group_name: Any): ...
