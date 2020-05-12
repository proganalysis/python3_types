# (generated with --quick)

from typing import Any, List, TypeVar

DatasetDownloader: Any
argparse: module
dataset: FornesMusicSymbolsDatasetDownloader
flags: argparse.Namespace
os: module
parser: argparse.ArgumentParser
unparsed: List[str]

AnyStr = TypeVar('AnyStr', str, bytes)

class FornesMusicSymbolsDatasetDownloader(Any):
    __doc__: str
    def _FornesMusicSymbolsDatasetDownloader__fix_capital_file_endings(self, absolute_path_to_temp_folder) -> None: ...
    def download_and_extract_dataset(self, destination_directory) -> None: ...
    def get_dataset_download_url(self) -> str: ...
    def get_dataset_filename(self) -> str: ...

def glob(pathname: AnyStr, *, recursive: bool = ...) -> List[AnyStr]: ...
