from typing import Any, Dict

StringsRow = Dict[str, str]
StringsDict = Dict[str, StringsRow]
_cache: Dict[str, StringsDict]

def load(fp: Any) -> StringsDict: ...
def load_globalstrings(locale: Any=...) -> StringsDict: ...
