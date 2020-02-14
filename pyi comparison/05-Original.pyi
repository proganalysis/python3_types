# (generated with --quick)

from typing import Any, Dict, List, Union

BASE_URL: str
BeautifulSoup: Any
LOCATION_LOOKUP: Dict[str, str]
re: module
requests: module

def _get_laundry_soup(building_name: str) -> Any: ...
def get_status_detailed(building_name: str) -> List[Dict[str, Union[int, str]]]: ...
def get_status_simple(building_name: str) -> Dict[str, str]: ...
