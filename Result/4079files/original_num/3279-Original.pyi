# (generated with --quick)

import kyoukai.asphalt
import kyoukai.route
import kyoukai.routegroup
import kyoukai.testing
from typing import Any, Dict, Tuple, Type, TypeVar
import werkzeug.exceptions
import werkzeug.formparser

Blueprint: Any
FormDataParser: Type[werkzeug.formparser.FormDataParser]
HTTPRequestContext: Type[kyoukai.asphalt.HTTPRequestContext]
Kyoukai: Any
KyoukaiComponent: Type[kyoukai.asphalt.KyoukaiComponent]
RequestEntityTooLarge: Type[werkzeug.exceptions.RequestEntityTooLarge]
Route: Type[kyoukai.route.Route]
RouteGroup: Type[kyoukai.routegroup.RouteGroup]
TestKyoukai: Type[kyoukai.testing.TestKyoukai]
__all__: Tuple[str, str, str, str, str, str, str]
__version__: Any
json: module

_T0 = TypeVar('_T0')

def _parse_json(parser: werkzeug.formparser.FormDataParser, stream: _T0, mimetype, content_length, options) -> Tuple[_T0, Any, Dict[nothing, nothing]]: ...
