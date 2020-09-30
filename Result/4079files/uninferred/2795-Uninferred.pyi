from setuptools import Command
from typing import Any

NAME: str
DESCRIPTION: str
URL: str
EMAIL: str
AUTHOR: str
REQUIRES_PYTHON: str
VERSION: Any
REQUIRED: Any
HERE: Any
LONG_DESC: Any
ABOUT: Any

class UploadCommand(Command):
    description: str = ...
    user_options: Any = ...
    @staticmethod
    def status(string: Any) -> None: ...
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
