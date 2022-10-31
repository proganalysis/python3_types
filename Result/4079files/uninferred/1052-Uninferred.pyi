from peewee import *
from typing import Any, Optional

class Reader:
    fh: Any = ...
    delimiter: Any = ...
    kws: Any = ...
    def __init__(self, fh: Any, delimiter: str = ..., **kws: Any) -> None: ...
    def __aiter__(self): ...
    async def __anext__(self): ...

class Get_Reader:
    file_or_name: Any = ...
    reader_kwargs: Any = ...
    is_file: bool = ...
    is_io: bool = ...
    def __init__(self, file_or_name: Any, **reader_kwargs: Any) -> None: ...
    fh: Any = ...
    async def __aenter__(self): ...
    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any) -> None: ...

class _CSVReader:
    def get_reader(self, file_or_name: Any, **reader_kwargs: Any): ...

def convert_field(field_class: Any, **field_kwargs: Any): ...

class RowConverter(_CSVReader):
    date_formats: Any = ...
    datetime_formats: Any = ...
    database: Any = ...
    has_header: Any = ...
    sample_size: Any = ...
    def __init__(self, database: Any, has_header: bool = ..., sample_size: int = ...) -> None: ...
    def matches_date(self, value: Any, formats: Any): ...
    def is_integer(self, value: Any): ...
    def is_float(self, value: Any): ...
    def is_datetime(self, value: Any): ...
    def is_date(self, value: Any): ...
    def default(self, value: Any): ...
    async def extract_rows(self, file_or_name: Any, **reader_kwargs: Any): ...
    def get_checks(self): ...
    def analyze(self, rows: Any): ...

class Loader(_CSVReader):
    file_or_name: Any = ...
    fields: Any = ...
    field_names: Any = ...
    has_header: Any = ...
    sample_size: Any = ...
    converter: Any = ...
    reader_kwargs: Any = ...
    filename: Any = ...
    database: Any = ...
    model: Any = ...
    db_table: Any = ...
    def __init__(self, db_or_model: Any, file_or_name: Any, fields: Optional[Any] = ..., field_names: Optional[Any] = ..., has_header: bool = ..., sample_size: int = ..., converter: Optional[Any] = ..., db_table: Optional[Any] = ..., pk_in_csv: bool = ..., **reader_kwargs: Any) -> None: ...
    def clean_field_name(self, s: Any): ...
    def get_converter(self): ...
    def analyze_csv(self) -> None: ...
    def get_model_class(self, field_names: Any, fields: Any): ...
    async def load(self): ...

async def aioload_csv(db_or_model: Any, file_or_name: Any, fields: Optional[Any] = ..., field_names: Optional[Any] = ..., has_header: bool = ..., sample_size: int = ..., converter: Optional[Any] = ..., db_table: Optional[Any] = ..., pk_in_csv: bool = ..., **reader_kwargs: Any): ...