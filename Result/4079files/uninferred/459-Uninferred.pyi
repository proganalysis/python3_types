from django.db import models
from typing import Any

class Environment(models.Model):
    name: Any = ...
    alias: Any = ...
    order: Any = ...
    fallback: Any = ...
    is_active: Any = ...
    created_at: Any = ...
    updated_at: Any = ...
    objects: Any = ...
    class Meta:
        verbose_name: Any = ...
        verbose_name_plural: Any = ...
        ordering: Any = ...
    def __str__(self): ...
    def natural_key(self): ...
    @property
    def is_base(self): ...