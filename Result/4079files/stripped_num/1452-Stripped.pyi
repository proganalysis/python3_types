# (generated with --quick)

from typing import Any

BASE: Any
BUTTONS_INSERTION_LOCK: threading._RLock
Boolean: Any
Column: Any
Integer: Any
NOTES_INSERTION_LOCK: threading._RLock
SESSION: Any
String: Any
Types: Any
UnicodeText: Any
distinct: Any
func: Any
threading: module

class Buttons(Any):
    __tablename__: str
    chat_id: Any
    id: Any
    name: Any
    note_name: Any
    same_line: Any
    url: Any
    def __init__(self, chat_id, note_name, name, url, same_line = ...) -> None: ...

class Notes(Any):
    __tablename__: str
    chat_id: Any
    file: Any
    has_buttons: Any
    is_reply: Any
    msgtype: Any
    name: Any
    value: Any
    def __init__(self, chat_id, name, value, msgtype, file = ...) -> None: ...
    def __repr__(self) -> str: ...

def add_note_button_to_db(chat_id, note_name, b_name, url, same_line) -> None: ...
def add_note_to_db(chat_id, note_name, note_data, msgtype, buttons = ..., file = ...) -> None: ...
def get_all_chat_notes(chat_id) -> Any: ...
def get_buttons(chat_id, note_name) -> Any: ...
def get_note(chat_id, note_name) -> Any: ...
def migrate_chat(old_chat_id, new_chat_id) -> None: ...
def num_chats() -> Any: ...
def num_notes() -> Any: ...
def rm_note(chat_id, note_name) -> bool: ...
