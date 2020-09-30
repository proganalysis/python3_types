# (generated with --quick)

from typing import Any

FormView: Any
Order: Any
Poloniex: Any
TemplateView: Any
constants: Any
forms: Any
json: module
messages: Any
models: Any
redirect: Any
render: Any
reverse: Any

class AccountPageView(Any):
    form_class: Any
    template_name: str
    def form_valid(self, form) -> Any: ...
    def get_context_data(self, **kwargs) -> Any: ...

class DashboardView(Any):
    template_name: str
    def get(self, request, *args, **kwargs) -> Any: ...

class FAQView(Any):
    template_name: str

class PortfolioView(Any):
    template_name: str
    def get(self, request, *args, **kwargs) -> Any: ...
