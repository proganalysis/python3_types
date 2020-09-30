from django.db.models import QuerySet
from typing import Any

class FuzzyCountQuerySet(QuerySet):
    def fuzzy_count(self): ...

FuzzyCountManager: Any
