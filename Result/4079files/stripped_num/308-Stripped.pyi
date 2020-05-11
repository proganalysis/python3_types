# (generated with --quick)

from typing import Any, Dict, Generator, Tuple, Type, TypeVar

docutils: module
sphinx: Any

_T3 = TypeVar('_T3')
_T4 = TypeVar('_T4')

class AnsibleDomain(Any):
    __doc__: str
    directives: Dict[str, Type[AnsibleRoleDirective]]
    initial_data: Dict[str, Dict[nothing, nothing]]
    label: str
    name: str
    object_types: Dict[str, Any]
    roles: Dict[str, AnsibleRoleRole]
    def clear_doc(self, doc) -> None: ...
    def get_objects(self) -> Generator[Tuple[Any, Any, str, Any, str, int], Any, None]: ...
    def resolve_any_xref(self, env, fromdocname, builder, type, target, node, contnode) -> None: ...
    def resolve_xref(self, env, fromdocname, builder, type, target, node, contnode) -> Any: ...

class AnsibleRoleDirective(Any):
    doc_field_types: list
    has_content: bool
    option_spec: Dict[str, Any]
    required_arguments: int
    def add_target_and_index(self, name, sig, signode) -> None: ...
    def handle_signature(self, sig, signode) -> str: ...

class AnsibleRoleRole(Any):
    def process_link(self, env, refnode, has_explicit_title, title: _T3, target: _T4) -> Tuple[_T3, _T4]: ...

def setup(app) -> None: ...
