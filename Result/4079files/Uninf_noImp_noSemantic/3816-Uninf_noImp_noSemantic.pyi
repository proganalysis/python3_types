from django.views.generic import TemplateView
from rinzler import Rinzler
from rinzler.core.route_mapping import RouteMapping

__author__: str

class MainController(TemplateView):
    @staticmethod
    def connect(app: Rinzler) -> RouteMapping: ...
