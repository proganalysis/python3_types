from django.forms import ModelForm
from typing import Any

class PostForm(ModelForm):
    class Meta:
        model: Any = ...
        fields: str = ...
    tags: Any = ...