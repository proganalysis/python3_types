# (generated with --quick)

from typing import Any, Callable, Dict, Optional, TypeVar

CLASS2DEFAULT_CUTOFF: Any
NEGATIVE_CLASS: Any
NEUTRAL_CLASS: Any
Name2Proba: Any
PACKAGE_ROOT: Any
POSITIVE_CLASS: Any
_CLASS2PROB: Dict[Any, float]
_DATA_ROOT: str
_FEMALE_NAME_AUGMENTATION_NUM: int
_LOGGER: Any
_NEUTRAL_NAME_AUGMENTATION_NUM: int
_PROCESSED_DATA_PATH: str
_RAW_DATA_ROOT: str
_TEST_DATA_SIZE: int
__author__: str
compute_gender_probas: Any
gen_name_gender_from_csv: Any
gen_triples_from_file: Any
get_logger: Any
np: module
os: module
pickle: module

_T0 = TypeVar('_T0')

def _augment_full_names(name2proba: _T0, gender) -> _T0: ...
def _process_common_names(name2proba: _T0) -> _T0: ...
def _process_csv(name2probfa: _T0) -> _T0: ...
def _process_dbpedia(name2proba: _T0) -> _T0: ...
def _process_us_stats(name2proba: _T0, start_year = ...) -> _T0: ...
def main() -> None: ...
def shuffle(x: list, random: Optional[Callable[[], float]] = ...) -> None: ...
