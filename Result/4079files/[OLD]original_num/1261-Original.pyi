# (generated with --quick)

from typing import Any, List, Type

AddNoteMethodType: Any
Note: Any
categories: Any
headers: Any
levels: Any
rfc7234: Any

class AGE_NEGATIVE(Any):
    category: Any
    level: Any
    summary: str
    text: str

class AGE_NOT_INT(Any):
    category: Any
    level: Any
    summary: str
    text: str

class AgeTest(Any):
    expected_err: List[nothing]
    expected_out: int
    inputs: List[bytes]
    name: str

class CharAgeTest(Any):
    expected_err: List[Type[AGE_NOT_INT]]
    expected_out: None
    inputs: List[bytes]
    name: str

class MultipleAgeTest(Any):
    expected_err: list
    expected_out: int
    inputs: List[bytes]
    name: str

class NegAgeTest(Any):
    expected_err: List[Type[AGE_NEGATIVE]]
    expected_out: None
    inputs: List[bytes]
    name: str

class age(Any):
    canonical_name: str
    deprecated: bool
    description: str
    list_header: bool
    reference: str
    syntax: bool
    valid_in_requests: bool
    valid_in_responses: bool
    def parse(self, field_value: str, add_note) -> int: ...
