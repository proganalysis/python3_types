# (generated with --quick)

import decimal
from typing import Any, Callable, Dict, List, Tuple, Type

App: Any
Builder: Any
ContextMenu: Any
Decimal: Type[decimal.Decimal]
Factory: Any
ObjectProperty: Any
_: Any

class AddressesDialog(Any):
    app: Any
    callback: Any
    context_menu: Any
    menu_actions: List[Tuple[Any, Callable[[Any], Any]]]
    screen: Any
    def __init__(self, app, screen, callback) -> None: ...
    def do_use(self, obj) -> None: ...
    def do_view(self, obj) -> None: ...
    def ext_search(self, card, search) -> Any: ...
    def get_card(self, addr, balance, is_used, label) -> Dict[str, Any]: ...
    def hide_menu(self) -> None: ...
    def show_menu(self, obj) -> None: ...
    def update(self) -> None: ...
