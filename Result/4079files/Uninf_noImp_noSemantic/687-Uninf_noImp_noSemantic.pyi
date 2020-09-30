from pybuilder.core import Project
from typing import Any

name: str
version: str
url: str
description: Any
summary: str
authors: Any
license: str
default_task: Any

def set_properties(project: Project) -> Any: ...
