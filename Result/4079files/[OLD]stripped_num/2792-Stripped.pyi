# (generated with --quick)

from typing import Any, Dict, List, Tuple, Type

AddNoteMethodType: Any
Note: Any
ParamDictType: Any
categories: Any
headers: Any
levels: Any
rfc7231: Any

class BadXXSSTest(Any):
    expected_err: list
    expected_out: None
    inputs: List[bytes]
    name: str

class OneBlockXXSSTest(Any):
    expected_err: List[Type[XSS_PROTECTION_BLOCK]]
    expected_out: Tuple[int, Dict[str, str]]
    inputs: List[bytes]
    name: str

class OneXXSSTest(Any):
    expected_err: List[Type[XSS_PROTECTION_ON]]
    expected_out: Tuple[int, Dict[nothing, nothing]]
    inputs: List[bytes]
    name: str

class XSS_PROTECTION_BLOCK(Any):
    category: Any
    level: Any
    summary: str
    text: str

class XSS_PROTECTION_OFF(Any):
    category: Any
    level: Any
    summary: str
    text: str

class XSS_PROTECTION_ON(Any):
    category: Any
    level: Any
    summary: str
    text: str

class ZeroXXSSTest(Any):
    expected_err: List[Type[XSS_PROTECTION_OFF]]
    expected_out: Tuple[int, Dict[nothing, nothing]]
    inputs: List[bytes]
    name: str

class x_xss_protection(Any):
    canonical_name: str
    deprecated: bool
    description: str
    list_header: bool
    reference: str
    syntax: str
    valid_in_requests: bool
    valid_in_responses: bool
    def parse(self, field_value, add_note) -> Tuple[int, Any]: ...
