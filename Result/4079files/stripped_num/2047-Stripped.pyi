# (generated with --quick)

from typing import Any, Dict

datetime: module
operator: module
parse: module
pathlib: module
types: module

class Project:
    __doc__: str
    analysis: types.SimpleNamespace
    claimed_commits: bool
    found_names: set
    name: Any
    repositories: tuple
    def __init__(self, person, name, *repos) -> None: ...
    def _analyze(self, name, commits) -> None: ...
    def _coalesce_author(self, name, commits_by_author) -> Any: ...
    def _commits_by_author(self, commits) -> Dict[Any, list]: ...
    def _create_stats(self, date_range, commit_count) -> types.SimpleNamespace: ...
    def _sort_by_date(self, commits) -> list: ...
