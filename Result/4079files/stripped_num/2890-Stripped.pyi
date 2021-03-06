# (generated with --quick)

import flask.app
import flask.wrappers
import odie
from typing import Any, Callable, Sequence, Type, Union

ClientError: Type[odie.ClientError]
Flask: Type[flask.app.Flask]
PdfFileReader: Any
PdfReadError: Any
ROUTE_ID: int
Response: Type[flask.wrappers.Response]
Schema: Any
app: flask.app.Flask
config: Any
datetime: module
fields: Any
inspect: Any
json: module
marshmallow: Any
os: module
reference: Any
request: flask.wrappers.Request
sqla: Any

class NonConfidentialException(Exception): ...

class PaginatedResult(object):
    __doc__: str
    data: Any
    pagination: Any
    schema: Any
    def __init__(self, pagination, schema) -> None: ...

class PaginatedResultSchema(Any):
    data: Any
    number_of_pages: Any
    page: Any
    total: Any

def api_route(url, *args, **kwargs) -> Callable[[Any], Any]: ...
def deserialize(schema) -> Callable[[Any], Any]: ...
def document_path(id) -> str: ...
def end_of_local_date(d) -> datetime.datetime: ...
def endpoint(query_fn, schemas = ..., allow_delete = ..., paginate_many = ...) -> Callable: ...
def event_stream(f) -> Callable: ...
def filtered_results(query, schema, paginate = ...) -> Any: ...
def get_user() -> Any: ...
def handle_client_errors(f) -> Callable: ...
def jsonify(*args, **kwargs) -> Union[str, flask.wrappers.Response]: ...
def jsonquery(query, json, **kwargs) -> Any: ...
def number_of_pages(document) -> Any: ...
def save_file(document, file_storage) -> None: ...
def serialize(data, schema, many = ...) -> Any: ...
def wraps(wrapped: Callable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable[[Callable], Callable]: ...
