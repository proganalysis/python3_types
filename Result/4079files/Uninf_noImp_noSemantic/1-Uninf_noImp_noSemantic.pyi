from imports import *
from bs4 import BeautifulSoup as BeautifulSoup
from typing import Any
from util.pollen_utils import pollen_url as pollen_url
from util.utils import batch_getterer as batch_getterer, batchify as batchify, collapse_dims as collapse_dims, ends_with as ends_with, flatten_multindex as flatten_multindex, mse as mse, ravel as ravel, repackage_hidden as repackage_hidden, to_sub_seqs as to_sub_seqs

ss: Any
mem: Any
rd: Any
pollen_date2df: Any
pollen_data: Any
poldf: Any
No: Any
poldf2: Any

def mkds_url(sdate: Any): ...

key: Any

def date_rng_gen(start: Any) -> None: ...
def gen_yr_rng(start: Any, backward: bool = ...): ...
def test_date_rng_gen() -> None: ...
def mktime(s: Any, hour: int = ...): ...
def camel2score(s: Any): ...
def parse_data(j: Any): ...

today: str
u: Any
r: Any

def sync_rdd(ss: Any, rd: Any, stdate: str = ...): ...
def accum(stdate: str = ...): ...

dat: Any
hrdfs: Any
dls: Any
crs: Any
_: Any
dailydf: Any

def concat(dfs: Any): ...
def rep_with_dummies_(df: Any, col: Any): ...
def rep_with_dummies(df: Any, cols: Any): ...

hr_dat2: Any
ns: Any
ncols: Any
cn: Any
