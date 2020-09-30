# (generated with --quick)

import sqlite3.dbapi2
from typing import TextIO

connexion: sqlite3.dbapi2.Connection
current: str
cursor: sqlite3.dbapi2.Cursor
file: str
hashlib: module
log: TextIO
os: module
requests: module
sqlite3: module
time: module

def add_file(path, file, hash_value, action, size) -> None: ...
def analyse(path) -> None: ...
def is_in_table(path, file) -> bool: ...
def md5(fname) -> str: ...
def parse(path, file) -> None: ...
def update_file(path, file, hash_value, action, size) -> None: ...
