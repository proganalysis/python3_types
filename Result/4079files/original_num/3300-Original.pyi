# (generated with --quick)

import pathlib
from typing import Any, Type

Github: Any
Path: Type[pathlib.Path]
Repo: Any
Repository: Any
UnknownObjectException: Any
add: Any
commit: Any
datetime: module
os: module
push: Any
subprocess: module
tag_list: Any

def build() -> None: ...
def commit_and_push(version: str, repository) -> None: ...
def create_github_release(repository, version: str) -> None: ...
def get_repo(github_token: str, github_owner: str) -> Any: ...
def get_version() -> str: ...
def main() -> None: ...
def update_changelog(version: str) -> None: ...
