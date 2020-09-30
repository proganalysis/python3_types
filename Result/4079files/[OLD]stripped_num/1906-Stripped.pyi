# (generated with --quick)

from typing import Any, Dict, List, Mapping, Optional, Tuple

HERE: pathlib.Path
SETUP_TEMPLATE: str
__updated__: str
pathlib: module
runpy: module
setuptools: module
sys: module
t: module

class Package:
    __doc__: str
    author: str
    author_email: str
    classifiers: List[str]
    description: str
    download_url: str
    entry_points: Mapping[str, List[str]]
    exclude_package_data: Dict[nothing, nothing]
    extras_require: Mapping[str, List[str]]
    install_requires: List[str]
    keywords: List[str]
    license_str: str
    long_description: str
    long_description_content_type: str
    name: str
    package_data: Dict[nothing, nothing]
    packages: List[str]
    python_requires: str
    root_directory: str
    test_suite: str
    url: str
    version: str
    @classmethod
    def parse_readme(cls, readme_path = ..., encoding = ...) -> Tuple[str, str]: ...
    @classmethod
    def prepare(cls) -> None: ...
    @classmethod
    def setup(cls) -> None: ...
    @classmethod
    def try_fields(cls, *names) -> Any: ...

def find_packages(root_directory = ...) -> Any: ...
def find_required_python_version(classifiers, version_prefix = ..., only_suffix = ...) -> Optional[str]: ...
def find_version(package_name, version_module_name = ..., version_variable_name = ...) -> Any: ...
def parse_requirements(requirements_path = ...) -> list: ...
def partition_version_classifiers(classifiers, version_prefix = ..., only_suffix = ...) -> Tuple[List[Tuple[int, ...]], List[Tuple[int, ...]]]: ...
def resolve_relative_rst_links(text, base_link) -> Any: ...
