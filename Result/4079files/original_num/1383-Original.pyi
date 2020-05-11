# (generated with --quick)

import enum
from typing import Any, List, Optional, Type

ColorScheme: Any
IntEnum: Type[enum.IntEnum]
MONOSPACE_FONT: Any
MyTreeView: Any
QAbstractItemView: Any
QFont: Any
QMenu: Any
QStandardItem: Any
QStandardItemModel: Any
Qt: Any
_: Any

class UTXOList(Any):
    Columns: type
    filter_columns: list
    headers: dict
    utxo_dict: dict
    wallet: Any
    def __init__(self, parent = ...) -> None: ...
    def create_menu(self, position) -> None: ...
    def get_selected_outpoints(self) -> Optional[List[str]]: ...
    def insert_utxo(self, idx, x) -> None: ...
    def update(self) -> None: ...
