from base.viewmixins import LoginRequiredMixin
from django.views.generic import TemplateView
from typing import Any

class UserspaceHomeView(LoginRequiredMixin, TemplateView):
    template_name: str = ...
    def get(self, request: Any): ...
