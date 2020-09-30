# (generated with --quick)

from typing import Any, Dict, Generator, List, Optional, Tuple

MAX_NUM_FILES_TO_MERGE_AT_ONCE: int
MIN_NUM_FILES_TO_MERGE_AT_ONCE: int
PheWebError: Any
ProgressBar: Any
VariantFileReader: Any
VariantFileWriter: Any
bisect: module
blist: Any
chrom_order: Any
common_filepaths: Any
conf: Any
contextlib: module
get_dated_tmp_path: Any
get_maf: Any
get_num_procs: Any
get_phenolist: Any
get_tmp_path: Any
indent: Any
make_basedir: Any
mtime: Any
multiprocessing: module
os: module
random: module
traceback: module

class MergeManager:
    __doc__: str
    files: List[Dict[str, Any]]
    n_procs: Any
    def __init__(self) -> None: ...
    def apply_ret(self, ret) -> None: ...
    def put_task(self, taskq) -> Optional[str]: ...

class VariantListMerger:
    __doc__: str
    _q: Any
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...
    @staticmethod
    def _key_from_variant(v) -> Tuple[Any, Any, Any, Any]: ...
    def insert(self, variant, reader_id) -> None: ...
    def pop(self) -> Any: ...

def apply_maf_cutoff(variants, pheno) -> Generator[Any, Any, None]: ...
def merge(files_to_merge, out_filepath) -> Generator[Dict[str, str], Any, None]: ...
def mp_target(taskq, retq) -> None: ...
def run(argv) -> None: ...
