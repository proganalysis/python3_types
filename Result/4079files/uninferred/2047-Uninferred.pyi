from typing import Any

class Project:
    name: Any = ...
    repositories: Any = ...
    claimed_commits: bool = ...
    analysis: Any = ...
    def __init__(self, person: Any, name: Any, *repos: Any) -> None: ...
    def _analyze(self, name: Any, commits: Any): ...
    def _create_stats(self, date_range: Any, commit_count: Any): ...
    def _commits_by_author(self, commits: Any): ...
    found_names: Any = ...
    def _coalesce_author(self, name: Any, commits_by_author: Any): ...
    def _sort_by_date(self, commits: Any): ...