# (generated with --quick)

from typing import Any, Dict, Type

BaseResponseObject: Any
PaginatedListProxy: Any
User: Any
datetime: Type[datetime.datetime]
objects: Any
return_key: Any

class PartialRepo(Any):
    _default_urls: Dict[str, str]
    _url: str
    clone_url: Any
    description: Any
    fork: Any
    full_name: Any
    git_url: Any
    homepage: Any
    html_url: Any
    id: Any
    mirror_url: Any
    name: Any
    owner: Any
    private: Any
    ssh_url: Any
    svn_url: Any
    @staticmethod
    def _get_key_mappings() -> Dict[str, Any]: ...
    def _get_related_fetch_params(self) -> Dict[str, dict]: ...
    def get_assignees(self) -> Any: ...
    def get_blobs(self) -> Any: ...
    def get_branch(self, branch) -> coroutine: ...
    def get_branches(self) -> Any: ...
    def get_collaborators(self) -> Any: ...
    def get_comments(self) -> Any: ...
    def get_commits(self) -> Any: ...
    def get_contributors(self) -> Any: ...
    def get_events(self) -> Any: ...
    def get_forks(self) -> Any: ...
    def get_issues(self) -> Any: ...
    def get_pull_requests(self) -> Any: ...
    def get_stargazers(self) -> Any: ...

class Repo(PartialRepo):
    created_at: Any
    default_branch: Any
    forks_count: Any
    has_downloads: Any
    has_issues: Any
    has_pages: Any
    has_wiki: Any
    language: Any
    open_issues_count: Any
    permissions: Any
    pushed_at: Any
    size: Any
    stargazers_count: Any
    updated_at: Any
    watchers_count: Any
