# (generated with --quick)

from typing import Any

Extension: Any

class FakeExtension(Any):
    accept_response: Any
    accepted_offer: Any
    name: str
    offer_response: Any
    offered: Any
    def __init__(self, offer_response = ..., accept_response = ...) -> None: ...
    def accept(self, offer) -> Any: ...
    def finalize(self, offer) -> None: ...
    def offer(self) -> Any: ...
