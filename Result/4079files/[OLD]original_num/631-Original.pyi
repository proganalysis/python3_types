# (generated with --quick)

from typing import Any, Coroutine, Dict

APP_CLIENT_ID: Any
APP_CLIENT_SECRET: Any
APP_ID: Any
APP_KEY: Any
AbstractAuthorizationPolicy: Any
AiohttpGitHubHandler: Any
BOT_NAME: Any
EncryptedCookieStorage: Any
GITTER_CHANNELS: Any
GITTER_TOKEN: Any
GitHubAppHandler: Any
GitterListener: Any
LOGLEVEL: str
SessionIdentityPolicy: Any
VERSION: Any
aiohttp: Any
aiohttp_jinja2: Any
authorized_userid: Any
base64: module
fernet: module
handle_errors: Any
jinja2: module
logger: logging.Logger
logging: module
markdown: Any
markupsafe: module
md2html: Any
navigation_bar: Any
os: module
setup_security: Any
setup_session: Any
subprocess: module
time: module
utils: Any
web_routes: Any

class AuthorizationPolicy(Any):
    __doc__: str
    app: Any
    def __init__(self, app) -> None: ...
    def authorized_userid(self, identity: str) -> coroutine: ...
    def permits(self, identity: str, permission: str, context = ...) -> Coroutine[Any, Any, bool]: ...

def jinja2_filter_markdown(text) -> markupsafe.Markup: ...
def jinja_defaults(request) -> Coroutine[Any, Any, Dict[str, Any]]: ...
def start() -> coroutine: ...
def start_with_celery() -> coroutine: ...
