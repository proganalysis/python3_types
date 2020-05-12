# (generated with --quick)

from typing import Any, Dict, List

SITECODE_TRANSLATORS: Dict[str, Any]
SVYDESIGN_COLS: List[str]
US_STATES_FIPS_INTS: Any
curry: Any
filter: Any
identity: Any
log: Any
logger: Any
map: Any
np: module
pd: Any
pdutil: Any
thread_last: Any
unique: Any
us: Any

def convert_cat_codes(s, fmt) -> Any: ...
def convert_cat_force(s, fmt) -> Any: ...
def eager_convert(s, fmt, lgr = ...) -> Any: ...
def eager_convert_categorical(s, lbls, fmts, lgr = ...) -> Any: ...
def filter_columns(df, facets, qids, lgr = ...) -> Any: ...
def find_na_synonyms(na_syns, df) -> Any: ...
def munge_df(df, r, lbls, facets, qids, na_syns, col_fn, fmts, fpc = ..., lgr = ...) -> Any: ...
