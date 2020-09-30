# (generated with --quick)

from typing import Any, List, Union

BACK_ALT: Any
BACK_PRI: Any
Back: Any
COLUMNS: list
Cmd2ArgumentParser: Any
EXAMPLE_ITERABLE_DATA: List[List[Union[float, int, str]]]
EXAMPLE_OBJECT_DATA: List[CityInfo]
EXTREMELY_HIGH_POULATION_DENSITY: int
OBJ_COLS: list
app: TableDisplay
bg: Any
city_data: List[Union[float, int, str]]
cmd2: Any
row: List[Union[float, int, str]]
sys: module
tf: Any

class CityInfo(object):
    __doc__: str
    _area: Any
    _population: Any
    city: Any
    continent: Any
    country: Any
    province: Any
    def __init__(self, city, province, country, continent, population, area) -> None: ...
    def get_area(self) -> Any: ...
    def get_population(self) -> Any: ...

class TableDisplay(Any):
    __doc__: str
    debug: bool
    do_object_table: Any
    do_table: Any
    def __init__(self) -> None: ...
    def ptable(self, rows, columns, grid_args, row_stylist) -> None: ...

def high_density_objs(row_obj) -> dict: ...
def high_density_tuples(row_tuple) -> dict: ...
def make_table_parser() -> Any: ...
def no_dec(num) -> str: ...
def pop_density(data) -> str: ...
def two_dec(num) -> str: ...
