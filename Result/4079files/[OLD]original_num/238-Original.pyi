# (generated with --quick)

from typing import Any

FormView: Any
JsonResponse: Any
Tradebot: Any
Wallet: Any
forms: Any
render: Any
simplejson: module

class BacktestingView(Any):
    form_class: Any
    template_name: str
    def form_valid(self, form) -> Any: ...

class LiveTestView(Any):
    form_class: Any
    template_name: str
    def form_valid(self, form) -> Any: ...
