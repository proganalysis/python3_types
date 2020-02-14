# (generated with --quick)

from typing import Any, Dict, List, TypeVar, Union

BASE_URL: str
BeautifulSoup: Any
LOCATION_LOOKUP: Dict[str, str]
re: module
requests: module

_T0 = TypeVar('_T0')

def _get_laundry_soup(building_name) -> Any: ...
def get_status_detailed(building_name) -> List[Dict[str, Any]]: ...
def get_status_simple(building_name: _T0) -> Dict[str, Union[int, _T0]]: ...
