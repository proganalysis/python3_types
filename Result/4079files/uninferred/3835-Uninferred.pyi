from typing import Any, Sequence

ROOT_DIR_PATH: Any
PRODUCTION_DOTENVS_DIR_PATH: Any
PRODUCTION_DOTENV_FILE_PATHS: Any
DOTENV_FILE_PATH: Any

def merge(output_file_path: str, merged_file_paths: Sequence[str], append_linesep: bool=...) -> None: ...
def main() -> None: ...
def test_merge(tmpdir_factory: Any, merged_file_count: int, append_linesep: bool) -> Any: ...
