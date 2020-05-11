# (generated with --quick)

import cogs.listings
import configparser
import models.character
from typing import Any, Coroutine, Dict, List, Tuple, Type

ADMIN_USER: str
Activity: Any
CHARACTER_CLASSES: List[str]
CHARACTER_CLASS_SHORT: Dict[str, str]
CHARACTER_COLLECTION: str
CLOUDINARY_API: str
CLOUDINARY_SECRET: str
CLOUD_NAME: str
CONFIG: configparser.ConfigParser
CONTENT_SENT_MESSAGE: str
Character: Type[models.character.Character]
ConfigParser: Type[configparser.ConfigParser]
DB_HOST: str
DB_NAME: str
DB_PASS: str
DB_USER: str
DESCRIPTION: str
HAS_CLOUD_STORAGE: bool
HEADERS: List[str]
HIST_COLLECTION: str
INITIAL_EXTENSIONS: Tuple[str, str, str, str, str, str, str]
Listing: Type[cogs.listings.Listing]
MEMBER_COLLECTION: str
Member: Any
OFFICER_MODE_MESSAGE: str
PIC_TAG: str
SERVER_COLLECTION: str
Server: Any
ServerSettings: Any
TOKEN: str
char1: Any
char2: Any
char3: Any
commands: Any
config: Any
member1: Any
member2: Any
mock: module
pytest: Any
server1: Any
server2: Any
sys: module

def __getattr__(name) -> Any: ...
def check_character_name(bot, char_class) -> Coroutine[Any, Any, bool]: ...
def codify(s) -> str: ...
def get_row(members, filter, num = ...) -> Any: ...
def is_officer_mode(server) -> Any: ...
def is_user_officer(roles) -> bool: ...
def logActivity(message, user) -> None: ...
def paginate(data) -> Any: ...
def print_error(error, message = ...) -> None: ...
def send_or_display(server, author, bot, content) -> Coroutine[Any, Any, None]: ...
def test_list() -> None: ...
