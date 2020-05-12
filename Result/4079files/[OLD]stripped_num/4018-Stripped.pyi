# (generated with --quick)

from typing import Any

datetime: module
json: module

class libJournal:
    json_location: Any
    def __init__(self) -> None: ...
    def add_entry(self, entry_title, content) -> None: ...
    def create_json(self, json_name) -> None: ...
    def delete_entry(self, entry_title) -> None: ...
    def find_entry(self, entry_title) -> bool: ...
    def get_date(self) -> str: ...
    def get_time(self) -> str: ...
    def open_json(self, json_location) -> Any: ...
    def read_entry(self, entry_title) -> Any: ...
    def set_json_location(self, json_location) -> None: ...
