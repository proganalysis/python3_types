# (generated with --quick)

import requests.sessions
from typing import Any, Generator
import xml.etree.ElementTree

Bill: Any
Division: Any
EDM: Any
ET: module
Member: Any
MemberList: Any
Parties: Any
datetime: module
parse_data: Any
requests: module
urllib: module

class Commons(House):
    members: Members
    name: str
    parl: Any
    def __init__(self, parl) -> None: ...
    def get_edms(self, limit = ..., page = ...) -> Generator[Any, Any, None]: ...

class House(object):
    members: Members
    name: Any
    parl: Any
    def __init__(self, name, parl) -> None: ...
    def recent_divisions(self, limit = ..., page = ..., since = ..., cachebust = ...) -> list: ...

class Members(object):
    _members: dict
    house: Any
    parl: Any
    def __init__(self, house) -> None: ...
    def current(self) -> Any: ...
    def from_id(self, member_id) -> Any: ...
    def from_url(self, url) -> Any: ...
    def from_vote(self, data) -> Any: ...

class Parliament(object):
    LDA_ENDPOINT: str
    MEMBERS_NAMES_ENDPOINT: str
    commons: Commons
    http: requests.sessions.Session
    lords: House
    parties: Any
    def get(self, path, limit = ..., page = ..., additional_params = ...) -> Any: ...
    def get_bills(self, limit = ..., page = ...) -> Generator[Any, Any, None]: ...
    def get_members(self, **kwargs) -> xml.etree.ElementTree.Element: ...
