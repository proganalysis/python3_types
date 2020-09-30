# (generated with --quick)

import flask.app
import flask.wrappers
from typing import Any, Dict, List, Tuple, Type

Babel: Any
Bcrypt: Any
CSRFProtect: Any
Compress: Any
Flask: Type[flask.app.Flask]
Locale: Any
LoginManager: Any
Migrate: Any
SQLAlchemy: Any
app: flask.app.Flask
babel: Any
bcrypt: Any
bp_action: Any
bp_admin: Any
bp_api: Any
bp_label: Any
bp_main: Any
bp_manage: Any
bp_stats: Any
bp_user: Any
bp_view: Any
config: Any
csrf: Any
db: Any
g: Any
language_list: List[str]
languages: Tuple[str, str]
lm: Any
locales: Dict[str, Any]
migrate: Any
pwgen: Any
request: flask.wrappers.Request
session: Any

def get_locale() -> Any: ...
def set_locale() -> None: ...
