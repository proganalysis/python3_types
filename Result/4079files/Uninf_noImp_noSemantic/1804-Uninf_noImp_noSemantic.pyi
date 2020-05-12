from typing import Any

dbc: Any
database: Any
modeldb: Any

def build_column_key(filename: Any, columname: Any): ...
def new_column(f: Any, c: Any, t: Any, sig: Any, n_data: Any, t_data: Any) -> None: ...
def get_numerical_signatures(): ...
def get_textual_signatures(): ...
def get_all_concepts(): ...
def peek_values(concept: Any, num: Any): ...
def get_values_and_type_of_concept(concept: Any): ...
def get_values_of_concept(concept: Any): ...
def get_fields_from_concept(concept: Any, arg1: Any, arg2: Any): ...
def get_all_num_cols_for_comp(): ...
def get_all_text_cols_for_comp(): ...
def search_keyword(keyword: Any): ...
def init(dataset_name: Any, create_index: bool = ...) -> None: ...
def main() -> None: ...
