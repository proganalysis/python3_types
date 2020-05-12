from github import Repository as Repository

def get_version() -> str: ...
def update_changelog(version: str) -> None: ...
def create_github_release(repository: Repository, version: str) -> None: ...
def commit_and_push(version: str, repository: Repository) -> None: ...
def get_repo(github_token: str, github_owner: str) -> Repository: ...
def build() -> None: ...
def main() -> None: ...
