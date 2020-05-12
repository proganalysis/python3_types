import seproxer.main
from typing import Any, Optional

logger: Any

def graceful_exit(seproxer_runner: seproxer.main.Seproxer, signum: Any, frame: Any) -> Any: ...
def main(args: Optional[Any] = ...) -> None: ...
