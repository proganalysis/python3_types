from ldap3 import ASYNC as ASYNC
from taiga.base.connectors.exceptions import ConnectorBaseException
from typing import Any

class KerberosLoginError(ConnectorBaseException): ...
class ADLoginError(ConnectorBaseException): ...
class LDAPLookupError(ConnectorBaseException): ...

AD_REALM: Any
AD_SHORT_REALM: Any
AD_ALLOWED_DOMAINS: Any
AD_DEFAULT_DOMAIN: Any
AD_LDAP_SERVER: Any
AD_LDAP_PORT: Any
AD_USE_SSL: Any
AD_SEARCH_BASE: Any
AD_SEARCH_FILTER: Any
AD_BIND_DN: Any
AD_BIND_PASSWORD: Any
AD_EMAIL_PROPERTY: Any
AD_FULLNAME_PROPERTY: Any

def do_ldap_search(username: str, password: str) -> tuple: ...
def login(email: str, password: str) -> tuple: ...
