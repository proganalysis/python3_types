# (generated with --quick)

from typing import Any, Dict, Set, Union

BASE: Any
BUTTON_LOCK: threading._RLock
Boolean: Any
CHAT_FILTERS: Dict[Any, list]
CUST_FILT_LOCK: threading._RLock
Column: Any
Integer: Any
SESSION: Any
String: Any
UnicodeText: Any
distinct: Any
func: Any
threading: module

class Buttons(Any):
    __tablename__: str
    chat_id: Any
    id: Any
    keyword: Any
    name: Any
    same_line: Any
    url: Any
    def __init__(self, chat_id, keyword, name, url, same_line = ...) -> None: ...

class CustomFilters(Any):
    __tablename__: str
    chat_id: Any
    has_buttons: Any
    has_markdown: Any
    is_audio: Any
    is_document: Any
    is_image: Any
    is_sticker: Any
    is_video: Any
    is_voice: Any
    keyword: Any
    reply: Any
    def __eq__(self, other) -> bool: ...
    def __init__(self, chat_id, keyword, reply, is_sticker = ..., is_document = ..., is_image = ..., is_audio = ..., is_voice = ..., is_video = ..., has_buttons = ...) -> None: ...
    def __repr__(self) -> str: ...

def __load_chat_filters() -> None: ...
def add_filter(chat_id, keyword, reply, is_sticker = ..., is_document = ..., is_image = ..., is_audio = ..., is_voice = ..., is_video = ..., buttons = ...) -> None: ...
def add_note_button_to_db(chat_id, keyword, b_name, url, same_line) -> None: ...
def get_all_filters() -> Any: ...
def get_buttons(chat_id, keyword) -> Any: ...
def get_chat_filters(chat_id) -> Any: ...
def get_chat_triggers(chat_id) -> Union[list, Set[nothing]]: ...
def get_filter(chat_id, keyword) -> Any: ...
def migrate_chat(old_chat_id, new_chat_id) -> None: ...
def num_chats() -> Any: ...
def num_filters() -> Any: ...
def remove_filter(chat_id, keyword) -> bool: ...
