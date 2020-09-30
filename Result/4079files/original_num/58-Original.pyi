# (generated with --quick)

from typing import Union

configparser: module
urllib: module

class SiteConfig:
    DEBUG: bool
    EMULATE: bool
    ESI_BASE_URL: str
    EVECENTRAL_CACHE_DIR: str
    EVECENTRAL_CACHE_HOURS: int
    EVEDB: str
    NAMES_DB: str
    PRICE_RESOLVER: str
    ROUTES_CACHE_DIR: str
    SESSION_FILES_DIR: str
    SESSION_REDIS_DB: Union[int, str]
    SESSION_REDIS_HOST: str
    SESSION_REDIS_PORT: Union[int, str]
    SESSION_TIME_MINUTES: int
    SESSION_TYPE: str
    SSO_CALLBACK_URL: str
    SSO_CLIENT_ID: str
    SSO_SCOPES: str
    SSO_SECRET_KEY: str
    SSO_USER_AGENT: str
    TEMPLATE_CACHE_DIR: str
    TEMPLATE_DIR: str
    ZKB_CACHE_DIR: str
    ZKB_CACHE_SQLITE: str
    ZKB_CACHE_TIME: int
    ZKB_CACHE_TYPE: str
    ZKB_KILLS_ON_PAGE: int
    ZKB_USE_EVEKILL: bool
    def __init__(self) -> None: ...
    def load(self, cfg_filename: str) -> None: ...
    def sso_login_url(self, optional_state: str = ...) -> str: ...
