from injector import Module
from peewee import Database
from typing import Any

class DatabaseModule(Module):
    def provide_db(self) -> Database: ...

DB_INJECTOR: Any

def get_db() -> Database: ...
