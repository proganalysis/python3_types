# (generated with --quick)

import abc
from typing import Any, Callable, Type, TypeVar
import zipfile

ABC: Type[abc.ABC]
ZipFile: Type[zipfile.ZipFile]
os: module
shutil: module
tqdm: Any
urllib2: module
urlparse: module

_FuncT = TypeVar('_FuncT', bound=Callable)

class DatasetDownloader(abc.ABC):
    __doc__: str
    def clean_up_temp_directory(self, temp_directory) -> None: ...
    @staticmethod
    def copytree(src, dst) -> None: ...
    @abstractmethod
    def download_and_extract_dataset(self, destination_directory) -> Any: ...
    def download_file(self, url, destination_filename = ...) -> Any: ...
    def extract_dataset(self, absolute_path_to_folder, dataset_filename = ...) -> None: ...
    @abstractmethod
    def get_dataset_download_url(self) -> Any: ...
    @abstractmethod
    def get_dataset_filename(self) -> Any: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
