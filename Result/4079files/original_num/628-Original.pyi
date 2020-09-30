# (generated with --quick)

from typing import Any

JSONField: Any
TimeStampedModel: Any
User: Any
_: Any
models: Any

class Author(Any):
    Meta: type
    name: Any
    def __str__(self) -> Any: ...

class Link(Any):
    __doc__: str
    cover: Any
    file: Any
    language: Any
    resource: Any
    title: Any
    url: Any

class Organization(Any):
    acronyms: Any
    contact: Any
    description: Any
    name: Any
    type: Any

class OrganizationType(Any):
    description: Any
    id: Any
    name: Any

class PublicationType(Any):
    Meta: type
    __doc__: str
    description: Any
    id: Any
    name: Any

class Resource(Any):
    __doc__: str
    author: Any
    cover: Any
    description: Any
    name: Any
    organization: Any
    pubtype: Any
    tag: Any
    user: Any
    year: Any

class Tag(Any):
    description: Any
    name: Any
