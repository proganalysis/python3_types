# (generated with --quick)

from typing import Any, Callable, Optional

Card: Any
__author__: str
translate: Any

class CardDeck(object):
    deck: list
    lang_id: str
    value_str: list
    def __init__(self, lang_id: str) -> None: ...
    def create_deck(self) -> list: ...
    def pick_one_card(self) -> Any: ...

def shuffle(x: list, random: Optional[Callable[[], float]] = ...) -> None: ...
