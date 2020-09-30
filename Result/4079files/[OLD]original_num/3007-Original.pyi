# (generated with --quick)

from typing import Any, Dict, Type

_ALLOWED_HTTP_METHOD: str
_AZURE_STORAGE_API_VERSION: str
_AZURE_STORAGE_CONN_STRING_ENV_NAME: str
_SAS_TOKEN_DEFAULT_TTL: int
base64: module
connString: str
datetime: Type[datetime.datetime]
func: Any
hashlib: module
hmac: module
json: module
logging: module
os: module
timedelta: Type[datetime.timedelta]
urllib: module

def generate_sas_token(storage_account, storage_key, permission, token_ttl, container_name, blob_name = ...) -> Dict[str, str]: ...
def main(req) -> str: ...
def write_http_response(status, body_dict) -> str: ...
