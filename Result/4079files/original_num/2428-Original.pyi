# (generated with --quick)

import collections
import datetime
import dateutil.parser
from typing import Any, Dict, IO, Optional, Type, TypeVar, Union

defaultdict: Type[collections.defaultdict]

_T = TypeVar('_T')

class Bill(Resource):
    date: None
    description: Any
    home_page: None
    parl: Any
    title: None
    type: None
    def __init__(self, parl) -> None: ...
    def fetch_data(self) -> None: ...

class Division(Resource):
    _data_fetched: bool
    abstain: int
    ayes: int
    contents: int
    date: None
    did_not_vote: int
    error_vote: int
    house: Any
    margin: int
    noes: int
    non_eligible: int
    not_contents: int
    parl: Any
    passed: Any
    resource: None
    suspended_expelled: int
    title: None
    uin: None
    votes: Dict[str, MemberList]
    def __eq__(self, other) -> Any: ...
    def __getattr__(self, name: str) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __init__(self, house) -> None: ...
    def _fetch_data(self) -> None: ...

class EDM(Resource):
    resource: None

class Member(Resource):
    _data_fetched: bool
    constituency: Any
    date_of_birth: Any
    display_name: Any
    dods_id: int
    end_date: Any
    full_name: Any
    gender: Any
    house: Any
    id: Any
    member_type: Any
    parl: Any
    party: Any
    pims_id: int
    start_date: Any
    def __getattr__(self, name: str) -> Any: ...
    def __init__(self, parl, house, member_id) -> None: ...
    def _fetch_data(self) -> None: ...
    def _populate_data(self, data) -> None: ...

class MemberList(list):
    def by_party(self) -> Dict[nothing, Any]: ...

class Resource(object):
    resource: None
    resource_id: int

def parse_data(data) -> Any: ...
def parse_date(timestr: Union[bytes, str, IO], parserinfo: Optional[dateutil.parser.parserinfo] = ..., **kwargs) -> datetime.datetime: ...
def parse_date_element(el) -> Optional[datetime.datetime]: ...
def total_ordering(cls: Type[_T]) -> Type[_T]: ...
