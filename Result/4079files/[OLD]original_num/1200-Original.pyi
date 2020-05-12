# (generated with --quick)

from typing import Any

AD_ALLOWED_DOMAINS: Any
AD_BIND_DN: Any
AD_BIND_PASSWORD: Any
AD_DEFAULT_DOMAIN: Any
AD_EMAIL_PROPERTY: Any
AD_FULLNAME_PROPERTY: Any
AD_LDAP_PORT: Any
AD_LDAP_SERVER: Any
AD_REALM: Any
AD_SEARCH_BASE: Any
AD_SEARCH_FILTER: Any
AD_SHORT_REALM: Any
AD_USE_SSL: Any
ASYNC: Any
BasicAuthError: Any
Connection: Any
ConnectorBaseException: Any
EmailValidator: Any
NONE: Any
SIMPLE: Any
SUBTREE: Any
SYNC: Any
Server: Any
ValidationError: Any
checkPassword: Any
settings: Any

class ADLoginError(Any): ...

class KerberosLoginError(Any): ...

class LDAPLookupError(Any): ...

def do_ldap_search(username: str, password: str) -> tuple: ...
def login(email: str, password: str) -> tuple: ...
