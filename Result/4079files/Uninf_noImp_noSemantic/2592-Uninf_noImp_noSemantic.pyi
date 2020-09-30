from setuptools.command.test import test as TestCommand
from typing import Any

long_description: Any

class UseToxError(TestCommand):
    def run_tests(self) -> None: ...
