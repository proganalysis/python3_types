# (generated with --quick)

import distutils.cmd
import distutils.dist
import distutils.extension
from typing import Any, List, Mapping, Tuple, Type, Union

APP_ID: str
APP_VERSION: str
LOCALE_DIR: str
PO_DIR: str
data_files: List[Tuple[str, List[str]]]
os: module
shutil: module

def compile_lang_files() -> List[Tuple[str, List[str]]]: ...
def setup(*, name: str = ..., version: str = ..., description: str = ..., long_description: str = ..., author: str = ..., author_email: str = ..., maintainer: str = ..., maintainer_email: str = ..., url: str = ..., download_url: str = ..., packages: List[str] = ..., py_modules: List[str] = ..., scripts: List[str] = ..., ext_modules: List[distutils.extension.Extension] = ..., classifiers: List[str] = ..., distclass: Type[distutils.dist.Distribution] = ..., script_name: str = ..., script_args: List[str] = ..., options: Mapping[str, Any] = ..., license: str = ..., keywords: Union[str, List[str]] = ..., platforms: Union[str, List[str]] = ..., cmdclass: Mapping[str, Type[distutils.cmd.Command]] = ..., data_files: List[Tuple[str, List[str]]] = ..., package_dir: Mapping[str, str] = ..., obsoletes: List[str] = ..., provides: List[str] = ..., requires: List[str] = ..., command_packages: List[str] = ..., command_options: Mapping[str, Mapping[str, Tuple[Any, Any]]] = ..., package_data: Mapping[str, List[str]] = ..., include_package_data: bool = ..., libraries: List[str] = ..., headers: List[str] = ..., ext_package: str = ..., include_dirs: List[str] = ..., password: str = ..., fullname: str = ..., **attrs) -> None: ...
