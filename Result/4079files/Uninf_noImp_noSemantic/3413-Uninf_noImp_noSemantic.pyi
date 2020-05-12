from britfoner import Seq as Seq, _MODEL_OUT as _MODEL_OUT
from typing import Any, Set

MAX_LENGTH: int
_dictionary: Any
_letter_index: Any
_inv_phone_index: Any
_model: Any
_EMPTY_SET: Any

def pronounce(word: str) -> Set[Seq]: ...
