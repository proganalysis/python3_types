# (generated with --quick)

import typing
from typing import Any, List, NoReturn, Tuple, Type

Counter: Type[typing.Counter]
REVIEWERS_LIMIT: int
STRIP_DOMAIN_USERNAMES: List[str]
__version__: str
argparse: module
get_reviewers: Any
json: module
os: module
pathlib: module
subprocess: module
sys: module
typing: module

class Config:
    BASE_BRANCH_DEFAULT: str
    COPY_DEFAULT: None
    DEFAULT_GLOBAL_JSON: str
    IGNORES_DEFAULT: str
    JSON_DEFAULT: str
    VERBOSE_DEFAULT: None
    base_branch: Any
    copy: Any
    ignores: list
    json: str
    verbose: Any
    def __init__(self) -> None: ...
    @staticmethod
    def default_global_json() -> str: ...
    def read_configs(self, args: argparse.Namespace) -> None: ...
    def read_from_args(self, args: argparse.Namespace) -> None: ...
    def read_from_json(self, args_json: str) -> None: ...

class FindArcCommitReviewers(FindLogReviewers):
    __doc__: str

class FindFileLogReviewers(FindReviewers):
    get_reviewers: Any
    def extract_username_from_shortlog(self, shortlog) -> Tuple[Any, int]: ...
    def get_changed_files(self) -> NoReturn: ...
    def get_log_reviewers_from_file(self, file_paths: List[str]) -> typing.Counter[str]: ...

class FindHistoricalReviewers(FindFileLogReviewers):
    get_reviewers: Any

class FindLogReviewers(FindFileLogReviewers):
    def get_changed_files(self) -> List[str]: ...

class FindReviewers:
    __init__: Any
    get_reviewers: Any
    def check_phabricator_activated(self, username) -> subprocess.Popen[bytes]: ...
    def extract_username_from_email(self, email) -> Any: ...
    def filter_phabricator_activated(self, all_users) -> list: ...
    def parse_phabricator(self, username: str, process: subprocess.Popen) -> str: ...
    def run_command(self, command) -> Any: ...

def main() -> None: ...
def show_reviewers(reviewer_list: List[str], copy_clipboard: bool) -> None: ...
