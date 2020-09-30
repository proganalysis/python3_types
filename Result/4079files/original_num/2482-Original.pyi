# (generated with --quick)

from typing import Any, Callable, List, Optional, Type, TypeVar

Github: Any
MAINTAINERS: List[str]
Milestone: Any
Repository: Any
argparse: module
datetime: module
os: module
re: module
urllib: module

_T = TypeVar('_T')

class Changelog:
    features: List[ChangelogItem]
    fixes: List[ChangelogItem]
    internals: List[ChangelogItem]
    def __repr__(self) -> str: ...
    def add_feature(self, feature: ChangelogItem) -> None: ...
    def add_fix(self, fix: ChangelogItem) -> None: ...
    def add_internal(self, internal: ChangelogItem) -> None: ...

class ChangelogItem:
    pull_request_id: int
    title: str
    username: str
    def __init__(self, pull_request_id: int, title: str, username: str) -> None: ...
    def display(self) -> str: ...

def collect_changelog(post_number: int, login_or_token: str, password: Optional[str] = ...) -> Changelog: ...
def contributors() -> None: ...
@overload
def dataclass(_cls: Type[_T]) -> Type[_T]: ...
@overload
def dataclass(*, init: bool = ..., repr: bool = ..., eq: bool = ..., order: bool = ..., unsafe_hash: bool = ..., frozen: bool = ...) -> Callable[[Type[_T]], Type[_T]]: ...
def main() -> None: ...
def new_post(args: argparse.Namespace) -> None: ...
