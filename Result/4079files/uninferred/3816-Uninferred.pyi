from django.views.generic import TemplateView
from rinzler import Rinzler as Rinzler
from rinzler.core.route_mapping import RouteMapping as RouteMapping

__author__: str

class MainController(TemplateView):
    @staticmethod
    def connect(app: Rinzler) -> RouteMapping: ...
