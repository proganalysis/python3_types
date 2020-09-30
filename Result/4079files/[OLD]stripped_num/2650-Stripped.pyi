# (generated with --quick)

import http.server
import provider.buienradar
import provider.fx
import provider.ns
import provider.ovapi
from typing import Dict, Type, Union

BuienRadarDataProvider: Type[provider.buienradar.BuienRadarDataProvider]
FxDataProvider: Type[provider.fx.FxDataProvider]
NSDepartureTimesProvider: Type[provider.ns.NSDepartureTimesProvider]
NSTravelAdviceProvider: Type[provider.ns.NSTravelAdviceProvider]
OvApiDataProvider: Type[provider.ovapi.OvApiDataProvider]
ROUTE_MAP: Dict[str, Type[Union[provider.buienradar.BuienRadarDataProvider, provider.fx.FxDataProvider, provider.ns.NSDepartureTimesProvider, provider.ns.NSTravelAdviceProvider, provider.ovapi.OvApiDataProvider]]]
SimpleHTTPRequestHandler: Type[http.server.SimpleHTTPRequestHandler]
json: module
urllib: module

class InfoPiRequestHandler(http.server.SimpleHTTPRequestHandler): ...
