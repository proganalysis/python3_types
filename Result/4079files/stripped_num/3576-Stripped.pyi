# (generated with --quick)

import decimal
from typing import Any, Generator, Type

API_KEY: Any
BASE_CURRENCY: Any
ConversionRate: Any
Decimal: Type[decimal.Decimal]
ENDPOINT_LATEST: str
ImproperlyConfigured: Any
logger: logging.Logger
logging: module
requests: module
settings: Any

def create_conversion_rates() -> Generator[Any, Any, None]: ...
def extract_rate(rates, currency) -> Any: ...
def get_latest_exchange_rates() -> Any: ...
def get_rates(qs, force_refresh = ...) -> Any: ...
def update_conversion_rates() -> Any: ...
