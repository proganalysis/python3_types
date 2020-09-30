# (generated with --quick)

from typing import Any, List, Optional, Tuple

ChandereError: Any
INVALID_CROSSLINK_TARGETS: List[str]
INVALID_URI_TARGETS: List[str]
VALID_CROSSLINK_TARGETS: List[Tuple[str, Tuple[str, Optional[str]]]]
VALID_URI_TARGETS: List[Tuple[str, Tuple[str, Optional[str]]]]
load_scraper: Any
pytest: Any
scraper: Any

def test_parse_invalid_crosslink_target() -> None: ...
def test_parse_invalid_uri_target() -> None: ...
def test_parse_valid_crosslink_target() -> None: ...
def test_parse_valid_uri_target() -> None: ...
