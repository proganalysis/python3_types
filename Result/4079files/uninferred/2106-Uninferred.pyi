from pathlib import Path
from typing import Any, Optional

logger: Any
EXTRACT_METHODS: Any

def get_latest_file_in_dir(dir_path: Path) -> Optional[Path]: ...
def banner_execute() -> Path: ...
def main(args: Any): ...
