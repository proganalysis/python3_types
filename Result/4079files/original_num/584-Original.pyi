# (generated with --quick)

from typing import Dict, List, TextIO, Union

USAGE: str
compl: str
completion: Dict[str, Dict[str, Dict[str, Union[bool, str, List[Union[int, str]]]]]]
default_completion_item: Dict[str, Union[bool, str]]
description: str
f: TextIO
flag: str
multiple: str
os: module
section: str
sys: module
zsh: str

def bash_completion() -> str: ...
def zsh_completion() -> str: ...
