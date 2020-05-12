# (generated with --quick)

from typing import Any, Dict, Generator, Tuple

NEGATIVE_CLASS: Any
NEUTRAL_CLASS: Any
POSITIVE_CLASS: Any
_CLASS_MAP: Dict[str, Any]
_FIRST_NAME_COLUMN: str
_GENDER_COLUMN: str
_LAST_NAME_COLUMN: str
_NAME_COLUMN: str
__author__: str
csv: module

class GenderCsvException(Exception):
    __doc__: str

def gen_name_gender_from_csv(file_path) -> Generator[Tuple[Any, Any], Any, None]: ...
