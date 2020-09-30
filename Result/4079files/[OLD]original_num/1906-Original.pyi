# (generated with --quick)

from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple

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
    def parse_readme(cls, readme_path: str = ..., encoding: str = ...) -> Tuple[str, str]: ...
    @classmethod
    def prepare(cls) -> None: ...
    @classmethod
    def setup(cls) -> None: ...
    @classmethod
    def try_fields(cls, *names) -> Any: ...

def find_packages(root_directory: str = ...) -> List[str]: ...
def find_required_python_version(classifiers: Sequence[str], version_prefix: str = ..., only_suffix: str = ...) -> Optional[str]: ...
def find_version(package_name: str, version_module_name: str = ..., version_variable_name: str = ...) -> str: ...
def parse_requirements(requirements_path: str = ...) -> List[str]: ...
def partition_version_classifiers(classifiers: Sequence[str], version_prefix: str = ..., only_suffix: str = ...) -> Tuple[List[str], List[str]]: ...
def resolve_relative_rst_links(text: str, base_link: str) -> str: ...
