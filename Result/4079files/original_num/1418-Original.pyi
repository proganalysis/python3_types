# (generated with --quick)

from typing import Any, TypeVar

graphene: Any
query_string: str
result: Any
schema: Any
uj: Any

_TCreatePerson = TypeVar('_TCreatePerson', bound=CreatePerson)

class CreatePerson(Any):
    Input: type
    ok: Any
    person: Any
    def mutate(self: _TCreatePerson, args, context, info) -> _TCreatePerson: ...

class LatLngInput(Any):
    lat: Any
    lng: Any

class LocationInput(Any):
    latlng: Any
    name: Any

class MyMutations(Any):
    create_person: Any

class Person(Any):
    age: Any
    name: Any

class PersonInput(Any):
    age: Any
    name: Any
