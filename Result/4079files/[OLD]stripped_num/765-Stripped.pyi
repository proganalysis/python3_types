# (generated with --quick)

from typing import Any, List, Optional, Tuple

PARTIES: List[Tuple[str, List[str], str]]

class Parties(object):
    parl: Any
    parties: List[Party]
    def __init__(self, parl) -> None: ...
    def all(self) -> List[Party]: ...
    def from_name(self, name) -> Optional[Party]: ...

class Party(object):
    abbreviation: Any
    alt_names: Any
    name: Any
    def __init__(self, name, alt_names, abbreviation) -> None: ...
    def __str__(self) -> Any: ...

def normalise_party_name(name) -> Any: ...
