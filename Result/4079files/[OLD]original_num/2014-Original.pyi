# (generated with --quick)

from typing import Any, NoReturn

QStandardItem: Any
QStandardItemModel: Any
load_workbook: Any

class ExcelIOException(Exception): ...

class ExcelQtConverter:
    __doc__: str
    file_name: Any
    px_workbook: Any
    def __init__(self, file_name) -> None: ...
    def from_model(self, qt_model, name) -> NoReturn: ...
    def save(self) -> None: ...
    def to_model(self, name, model_type = ..., header = ...) -> Any: ...

def convert_openpyxl_to_qtmodel(px_worksheet, model_type = ..., header = ...) -> Any: ...
