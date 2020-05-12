# (generated with --quick)

from typing import Any

ValidationError: Any
default_encoder: Any
falcon: Any
json: module
jsonschema: Any

def dump_json(req, resp, resource) -> None: ...
def parse_json(req, resp, resource, params) -> None: ...
def require_json(req, resp, resource, params) -> None: ...
def validate_json(req, resp, resource, params) -> None: ...
