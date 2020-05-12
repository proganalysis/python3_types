from django_extensions.db.models import TimeStampedModel
from typing import Any

class Resource(TimeStampedModel):
    year: Any = ...
    name: Any = ...
    description: Any = ...
    pubtype: Any = ...
    author: Any = ...
    organization: Any = ...
    tag: Any = ...
    cover: Any = ...
    user: Any = ...

class Link(TimeStampedModel):
    cover: Any = ...
    language: Any = ...
    title: Any = ...
    resource: Any = ...
    url: Any = ...
    file: Any = ...

class PublicationType(TimeStampedModel):
    id: Any = ...
    name: Any = ...
    description: Any = ...
    class Meta:
        verbose_name_plural: Any = ...
        ordering: Any = ...

class Author(TimeStampedModel):
    name: Any = ...
    def __str__(self): ...
    class Meta:
        verbose_name_plural: Any = ...
        ordering: Any = ...

class Organization(TimeStampedModel):
    name: Any = ...
    acronyms: Any = ...
    description: Any = ...
    contact: Any = ...
    type: Any = ...

class Tag(TimeStampedModel):
    name: Any = ...
    description: Any = ...

class OrganizationType(TimeStampedModel):
    id: Any = ...
    name: Any = ...
    description: Any = ...
