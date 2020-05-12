from crumpet.profiles import constants as constants
from django.views.generic import FormView, TemplateView
from typing import Any

class DashboardView(TemplateView):
    template_name: str = ...
    def get(self, request: Any, *args: Any, **kwargs: Any): ...

class AccountPageView(FormView):
    form_class: Any = ...
    template_name: str = ...
    def get_context_data(self, **kwargs: Any): ...
    def form_valid(self, form: Any): ...

class PortfolioView(TemplateView):
    template_name: str = ...
    def get(self, request: Any, *args: Any, **kwargs: Any): ...

class FAQView(TemplateView):
    template_name: str = ...
