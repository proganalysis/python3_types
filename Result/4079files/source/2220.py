from re import sub
from .constants import USER_NAME_REGEX

def to_name(name: str) -> str:
    if name is None:
        name = ""

    new_name: str = sub(USER_NAME_REGEX, "", name.lower()).strip()

    return new_name.lower()