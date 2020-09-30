# (generated with --quick)

import enum
from typing import Any, Dict, Type

ADDRESS_ID_1: Any
ADDRESS_MAPPINGS: Dict[Any, tuple]
Address: Any
AddressSchema: Any
DeleteAddressSchema: Any
Enum: Type[enum.Enum]
EnumField: Any
Namespace: Any
NewPersonBatchSchema: Any
NewPersonSchema: Any
OffsetLimitPageSchema: Any
Operation: Any
PERSON_ID_1: Any
PERSON_ID_2: Any
PERSON_ID_3: Any
PERSON_MAPPINGS: Dict[Any, tuple]
Person: Any
PersonBatchSchema: Any
PersonLookupSchema: Any
PersonSchema: Any
QueryStringList: Any
String: Any
address_delete: Any
address_retrieve: Any
address_search: Any
assert_that: Any
configure_crud: Any
contains_inanyorder: Any
create_object_graph: Any
equal_to: Any
is_: Any
person_create: Any
person_delete: Any
person_replace: Any
person_retrieve: Any
person_search: Any
person_update: Any
person_update_batch: Any

class SearchAddressPageSchema(Any):
    enum_param: Any
    list_param: Any

class TestCRUD:
    client: Any
    graph: Any
    def assert_response(self, response, status_code, data = ...) -> None: ...
    def setup(self) -> None: ...
    def test_count(self) -> None: ...
    def test_create(self) -> None: ...
    def test_create_empty_object(self) -> None: ...
    def test_create_malformed(self) -> None: ...
    def test_delete(self) -> None: ...
    def test_delete_not_found(self) -> None: ...
    def test_delete_with_params(self) -> None: ...
    def test_replace(self) -> None: ...
    def test_retrieve(self) -> None: ...
    def test_retrieve_not_found(self) -> None: ...
    def test_retrieve_qs(self) -> None: ...
    def test_reuse_search_self_link(self) -> None: ...
    def test_search(self) -> None: ...
    def test_search_with_context(self) -> None: ...
    def test_update(self) -> None: ...
    def test_update_batch(self) -> None: ...
    def test_update_not_found(self) -> None: ...

class TestEnum(enum.Enum):
    A: str
    B: str
    def __str__(self) -> Any: ...

def add_request_id(headers, response_data) -> None: ...
