# (generated with --quick)

from typing import Any, Dict, Type

ChainTransformer: Any
FIELDS: Dict[str, str]
LINK_FORMAT: str
Parser: Any
ctx: Any
tools: Any

class AdditionalInvestigator(Any):
    agent: Any
    schema: str

class FullNamePerson(Any):
    name: Any
    schema: str

class OtherInvestigator(Any):
    agent: Any
    schema: str

class Person(Any):
    family_name: Any
    given_name: Any

class PrincipalInvestigator(Any):
    agent: Any

class RRTransformer(Any):
    VERSION: int
    root_parser: Type[Registration]

class Registration(Any):
    Extra: type
    date_published: Any
    date_updated: Any
    description: Any
    identifiers: Any
    related_agents: Any
    title: Any
    def get_link(self, id) -> str: ...
    def split_names(self, obj) -> Any: ...

class WorkIdentifier(Any):
    uri: Any
