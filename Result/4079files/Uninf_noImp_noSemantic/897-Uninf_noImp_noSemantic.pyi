from typing import Any

docsdir: Any
builddir: Any
build_cmd: Any

def cmd() -> None: ...
def docs(p: str) -> str: ...

server: Any
