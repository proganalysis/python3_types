# (generated with --quick)

from typing import Any, NoReturn, Optional

QAbstractItemView: Any
QApplication: Any
QFrame: Any
QGridLayout: Any
QHBoxLayout: Any
QIcon: Any
QLabel: Any
QLineEdit: Any
QPushButton: Any
QStyleFactory: Any
QTableView: Any
QTreeView: Any
QWidget: Any
sys: module

class AbstractWindow(Any):
    __doc__: str
    def __init__(self) -> None: ...

class AccountingWindow(AbstractWindow):
    __doc__: str
    cart_model: Any
    customer_id_input: Any
    customer_id_label: Any
    height: int
    item_request_id_input: Any
    item_request_id_label: Any
    item_request_id_search: Any
    item_request_wrapper: Any
    items_model: Any
    left: Any
    right: Any
    title: str
    top: int
    width: int
    wrapper: Any
    def __init__(self, items, cart) -> None: ...
    def init_ui(self) -> None: ...
    def put_item_in_cart(self) -> None: ...

class MainWindow(AbstractWindow):
    __doc__: str
    accounting_window: Optional[AccountingWindow]
    cart_model: Any
    items_model: Any
    def __init__(self, items, cart) -> None: ...
    def init_ui(self) -> None: ...
    def on_click(self) -> None: ...

def main(items, cart) -> NoReturn: ...
