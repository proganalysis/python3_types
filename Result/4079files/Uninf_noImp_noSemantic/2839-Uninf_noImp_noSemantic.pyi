from flask import Flask
from grice.db_service import DBService
from typing import Any

log: Any

def parse_pagination(page: Any, per_page: Any): ...
def parse_filter(filter_string: str) -> Any: ...
def _parse_filter_obj_dict(filters: dict, from_url: bool=...) -> Any: ...
def parse_filter_obj(filters: Any, from_url: bool = ...): ...
def parse_filters(filter_description: dict) -> Any: ...
def parse_sort(sort_string: Any): ...
def parse_sorts(sort_list: Any): ...
def parse_join(join_str: Any, outer_join: bool) -> Any: ...
def parse_column_func(column_string: Any): ...
def parse_column_funcs(column_list: Any): ...
def parse_col_names(column_names: Any): ...
def parse_query_args(query_args: Any): ...
def table_not_found(name: Any): ...

class DBController:
    app: Any = ...
    db_service: Any = ...
    def __init__(self, app: Flask, db_service: DBService) -> None: ...
    def get_query_args(self): ...
    def tables_api(self): ...
    def table_api(self, name: Any): ...
    def query_api(self, name: Any): ...
    def tables_page(self): ...
    def table_page(self, name: Any): ...
    def chart_page(self, name: Any): ...
    def register_routes(self) -> None: ...