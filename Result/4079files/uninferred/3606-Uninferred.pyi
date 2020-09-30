from django.db.models.query import QuerySet
from typing import Any, Iterable, Type

def make_iterable(value: Any[object, Iterable, QuerySet], output_type: Type=...) -> Iterable: ...
