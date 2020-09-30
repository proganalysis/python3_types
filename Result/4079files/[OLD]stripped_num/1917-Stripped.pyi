# (generated with --quick)

from typing import Any, Tuple

datetime: module
fair_status: Any
naturaljoin: Any
timedelta: Any

class Auction(Any):
    begin: Any
    buyer: Any
    commit: Any
    commited: Any
    concrete_auction: Any
    effective_offer: Tuple[Any, Any]
    end: Any
    highest_bid: Any
    ordered_bids: Any
    place_bid: Any
    sells: Any
    status_text: Any
    var_entity: Any
    var_min: Any
    var_step: Any
    visible_sells: Any
    visible_wants: Any
    wants: Any
    def __str__(self) -> str: ...
    def _commit_buyer(self, t, var_amount) -> None: ...
    def _commit_seller(self, t, var_amount) -> None: ...
    def add_item(self, entity, amount, *args, **kwargs) -> None: ...
    def formatted_status(self, seller_name) -> Any: ...
    def is_active(self) -> Any: ...
    def minimum_bid(self) -> Any: ...

class AuctionException(Exception): ...

class AuctionedItem(Any):
    Meta: type
    __doc__: str
    amount: Any
    auction: Any
    entity: Any
    visible: Any
    will_sell: Any
    def __str__(self) -> str: ...
    def block_expect(self, t, bidder, coef = ...) -> None: ...
    def unblock(self, t, bidder) -> None: ...

class Bid(Any):
    Meta: type
    amount: Any
    auction: Any
    placed: Any
    team: Any
    def __repr__(self) -> str: ...
    def block(self, t, coef = ...) -> None: ...
    def unblock(self, t) -> None: ...

class BlackAuction(Auction):
    Meta: type
    description: str
    place_bid: Any
    seller_name: Any
    def commit(self) -> None: ...
    def get_seller_name(self) -> Any: ...
    def is_white(self) -> bool: ...

class WhiteAuction(Auction):
    Meta: type
    begin: Any
    create: Any
    description: Any
    end: Any
    seller: Any
    status_text: Any
    var_entity: Any
    var_min: Any
    var_step: Any
    def commit(self) -> None: ...
    @staticmethod
    def get_all_active() -> Any: ...
    def get_seller_name(self) -> Any: ...
    def is_white(self) -> bool: ...
    def place_bid(self, team, amount) -> Any: ...

def __getattr__(name) -> Any: ...
