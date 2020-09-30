from pybuilder.core import Logger, Project
from typing import Any

name: str
version: str
url: str
description: Any
summary: str
author: Any
authors: Any
license: str
default_task: Any
obsoletes: str

def set_properties(project: Project) -> Any: ...
def install_self(project: Project, logger: Logger) -> Any: ...
