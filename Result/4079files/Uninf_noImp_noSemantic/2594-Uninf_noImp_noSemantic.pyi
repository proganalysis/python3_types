from liquid_tags import register as register
from typing import Any

SYNTAX: str
AUDIO: Any
AUDIO_TYPEDICT: Any

def create_html(markup: Any): ...
def audio(preprocessor: Any, tag: Any, markup: Any): ...
