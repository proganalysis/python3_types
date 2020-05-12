# (generated with --quick)

from typing import Any, Optional, Union

Extension: Any

class FakeExtension(Any):
    accept_response: Optional[Union[bool, str]]
    accepted_offer: Optional[str]
    name: str
    offer_response: Optional[Union[bool, str]]
    offered: Optional[str]
    def __init__(self, offer_response: Union[bool, str] = ..., accept_response: Union[bool, str] = ...) -> None: ...
    def accept(self, offer: str) -> Union[bool, str]: ...
    def finalize(self, offer: str) -> None: ...
    def offer(self) -> Union[bool, str]: ...
