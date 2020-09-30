from setuptools.command.install import install
from typing import Any

class Installer(install):
    def run(self) -> None: ...

long_description: Any
