# (generated with --quick)

import __builtin__
from typing import Any, Type

AmountField: Any
FixedStrategyProfile: Any
PercentField: Any
PriceField: Any
RelativeStrategyProfile: Any
TradingStrategyProfile: Any
UserAccount: Any
constants: Any
datetime: Type[datetime.datetime]
models: Any
python_2_unicode_compatible: Any
user_signed_up: Any

class Balance(Any):
    Meta: type
    __doc__: str
    account: Any
    available: Any
    btc_value: Any
    created: Any
    on_orders: Any

class ExponentialMovingAverage(Any):
    Meta: type
    period: Any
    def __str__(self) -> str: ...

class IndicatorParameter(Any):
    name: Any
    parameter: Any

class Order(Any):
    Meta: __builtin__.type
    amount: Any
    created: Any
    date: Any
    order_number: Any
    price: Any
    status: Any
    ticker: Any
    type: Any
    updated: Any
    user_account: Any
    def __str__(self) -> str: ...

class SimpleMovingAverage(Any):
    Meta: type
    period: Any
    def __str__(self) -> str: ...

class Strategy(Any):
    Meta: type
    indicator: Any
    def __str__(self) -> str: ...

class Ticker(Any):
    Meta: type
    __doc__: str
    base_volume: Any
    high_24_hour: Any
    highest_bid: Any
    is_frozen: Any
    last: Any
    low_24_hour: Any
    lowest_ask: Any
    percent_change: Any
    quote_volume: Any
    symbol: Any
    ticker_id: Any
    def __str__(self) -> str: ...

def save_user_account_data(sender, request, user, **kwargs) -> None: ...
