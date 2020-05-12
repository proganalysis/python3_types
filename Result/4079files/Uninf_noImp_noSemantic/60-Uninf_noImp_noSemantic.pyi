from typing import Any

TEST_ARRAY: Any
TEST_NAME: Any

class CustomError(Exception): ...

class FastSchemas:
    @property
    def request(self): ...
    @property
    def response(self): ...

def fast_validate(schema: Any, data: Any): ...
def json_response_factory(data: Any): ...
def test_defaults() -> None: ...
def test_defaults_multiple() -> None: ...
def test_empty_array_ok() -> None: ...
def test_empty_array_fail() -> None: ...
def test_empty_object_ok() -> None: ...
def test_empty_object_fail() -> None: ...
def test_schema() -> None: ...
def test_schema_array() -> None: ...
def test_schema_array_empty() -> None: ...
def test_schema_default_values() -> None: ...
def test_schema_default_values_override_defaults() -> None: ...
def test_schema_custom_error_class() -> None: ...
def test_schema_custom_response_class() -> None: ...
def test_schema_custom_response_factory() -> None: ...
def test_schema_custom_response_factory_empty_response() -> None: ...
def test_schema_empty_response(kwargs: Any) -> None: ...
def test_schema_invalid_request(invalid_data: Any) -> None: ...
def test_shema_make_error_custom_error_class() -> None: ...
def test_schema_make_response_request_not_validated() -> None: ...
def test_schema_mapping_proxy_type(klass: Any) -> None: ...
def test_schema_multiple_request_data() -> None: ...
def test_schema_multiple_request_data_merged_class() -> None: ...
def test_schema_no_request_defined(module: Any) -> None: ...
def test_schema_no_response_defined(module: Any) -> None: ...
def test_fastjsonschema() -> None: ...
def test_invalid_default_value() -> None: ...
def test_tuple_is_array() -> None: ...
