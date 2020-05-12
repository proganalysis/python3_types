from typing import Any

DATA_KEY_UNIX_TIMESTAMP: str
DATA_KEY_LAST_PRICE: str
DATA_KEY_PRICE_24H_CHANGE: str
DATA_KEY_VOLUME_24H: str
DATA_KEY_NUMBER_OF_BUY_ORDERS: str
DATA_KEY_NUMBER_OF_SELL_ORDERS: str
DATA_KEY_BUY_PRICES: str
DATA_KEY_BUY_AMOUNTS: str
DATA_KEY_SELL_PRICES: str
DATA_KEY_SELL_AMOUNTS: str
DATA_REQUIREMENT_FULL_BOOK_ORDER: str

class DataInstance:
    data: Any = ...
    def __init__(self, raw_data: Any) -> None: ...
    def __str__(self): ...
