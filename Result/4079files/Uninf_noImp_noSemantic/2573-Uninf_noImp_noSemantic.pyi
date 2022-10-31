from collections import namedtuple
from typing import Any

Token = namedtuple('Token', ['kind', 'value'])

def validate_options(options_line: Any) -> None: ...
def _transform(kind: Any, text: Any): ...
def tokenize(options_line: Any): ...
def preprocess_options(options_line: Any): ...