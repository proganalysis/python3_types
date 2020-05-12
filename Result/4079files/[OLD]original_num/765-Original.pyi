# (generated with --quick)

from typing import Any, List, Optional, Tuple

PARTIES: List[Tuple[str, List[str], str]]

class Parties(object):
    parl: Any
    parties: List[Party]
    def __init__(self, parl) -> None: ...
    def all(self) -> List[Party]: ...
    def from_name(self, name: Optional[str]) -> Optional[Party]: ...

class Party(object):
    abbreviation: str
    alt_names: list
    name: str
    def __init__(self, name: str, alt_names: list, abbreviation: str) -> None: ...

def normalise_party_name(name) -> Any: ...
