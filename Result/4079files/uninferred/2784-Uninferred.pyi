from typing import Any

_NAME_COLUMN: str
_FIRST_NAME_COLUMN: str
_LAST_NAME_COLUMN: str
_GENDER_COLUMN: str
_CLASS_MAP: Any
__author__: str

class GenderCsvException(Exception): ...

def gen_name_gender_from_csv(file_path: Any): ...
