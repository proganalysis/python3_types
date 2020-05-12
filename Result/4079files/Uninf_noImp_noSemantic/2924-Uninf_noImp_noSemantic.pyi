from distutils.command.build import build
from typing import Any

class my_build(build):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
