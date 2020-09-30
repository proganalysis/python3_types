# (generated with --quick)

from typing import Any, Dict, List, Type, Union

SCHEMA: Dict[str, Union[str, Dict[str, Dict[str, str]], List[str]]]
base64: module
datetime: Type[datetime.datetime]
json: module
validate: Any

class FormDecodeError(Exception): ...

def _encode_form(form) -> bytes: ...
def decode_form(form_b64) -> Any: ...
def main() -> None: ...
