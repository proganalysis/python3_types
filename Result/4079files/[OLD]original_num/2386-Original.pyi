# (generated with --quick)

import time
from typing import Any, Optional, Tuple, Union

WDPASS: Any
WDUSER: Any
_: Any
brand_name: str
brand_qid: Any
brand_rxnorm: Any
df: Any
drug_qid: Any
emea: Any
login: Any
pd: Any
row: Any
tqdm: Any
url: Any
wdi_core: Any
wdi_helpers: Any
wdi_login: Any
wdi_property_store: Any

def create_ref_statement(emea_id, url) -> list: ...
def do_compound(brand_qid, drug_qid, brand_name) -> None: ...
def do_pharm_prod(drug_qid, brand_rxnorm, emea, url, brand_name) -> Any: ...
def gmtime(secs: Optional[float] = ...) -> time.struct_time: ...
def strftime(format: str, t: Union[time.struct_time, Tuple[int, int, int, int, int, int, int, int, int]] = ...) -> str: ...
def title_case(name) -> str: ...
