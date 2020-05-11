# (generated with --quick)

from typing import Any

BASE: Any
Boolean: Any
Column: Any
PERM_LOCK: threading._RLock
RESTR_LOCK: threading._RLock
SESSION: Any
String: Any
threading: module

class Permissions(Any):
    __tablename__: str
    audio: Any
    bots: Any
    chat_id: Any
    contact: Any
    document: Any
    forward: Any
    game: Any
    gif: Any
    location: Any
    photo: Any
    sticker: Any
    url: Any
    video: Any
    videonote: Any
    voice: Any
    def __init__(self, chat_id) -> None: ...
    def __repr__(self) -> str: ...

class Restrictions(Any):
    __tablename__: str
    chat_id: Any
    media: Any
    messages: Any
    other: Any
    preview: Any
    def __init__(self, chat_id) -> None: ...
    def __repr__(self) -> str: ...

def get_locks(chat_id) -> Any: ...
def get_restr(chat_id) -> Any: ...
def init_permissions(chat_id, reset = ...) -> Permissions: ...
def init_restrictions(chat_id, reset = ...) -> Restrictions: ...
def is_locked(chat_id, lock_type) -> Any: ...
def is_restr_locked(chat_id, lock_type) -> Any: ...
def migrate_chat(old_chat_id, new_chat_id) -> None: ...
def update_lock(chat_id, lock_type, locked) -> None: ...
def update_restriction(chat_id, restr_type, locked) -> None: ...
