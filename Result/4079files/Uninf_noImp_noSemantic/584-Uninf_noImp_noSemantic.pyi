from typing import Any

description: str
zsh: str
flag: str
multiple: str
section: str
default_completion_item: Any
completion: Any

def zsh_completion() -> str: ...
def bash_completion() -> str: ...
