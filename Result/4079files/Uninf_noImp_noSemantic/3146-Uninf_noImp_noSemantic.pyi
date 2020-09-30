from typing import Any

__author__: str
dir_path: Any
file_path: Any
translations: Any

def translate(string: str, language: str) -> str: ...
def translate_all(string: str) -> set: ...
