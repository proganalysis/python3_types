from typing import Any, Dict

def state_name_to_fips(name: str) -> int: ...
def state_name_to_abbr(name: str) -> str: ...
def state_fips_to_name(fips: int) -> str: ...
def state_abbr_to_name(abbr: str) -> str: ...
def state_fips_to_abbr(fips: int) -> str: ...
def state_abbr_to_fips(abbr: str) -> int: ...

_fips_to_name_xwalk: Dict[int, str]
_state_abbr_to_name: Dict[str, str]
_name_to_fips_xwalk: Any
_state_name_to_abbr: Any
state_fips_list: Any
state_names_list: Any
state_abbr_list: Any