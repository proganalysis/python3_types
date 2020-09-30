from setuptools import Command
from typing import Any

here: Any
NAME: str
DESCRIPTION: str
URL: str
EMAIL: str
AUTHOR: str
REQUIRES_PYTHON: str
VERSION: Any
EXTRAS: Any
REQUIRED: Any
long_description: Any
long_description = DESCRIPTION
about: Any

class UploadCommand(Command):
    description: str = ...
    user_options: Any = ...
    @staticmethod
    def status(s: Any) -> None: ...
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def twine_command(self): ...

class UploadTestCommand(UploadCommand):
    def twine_command(self): ...
