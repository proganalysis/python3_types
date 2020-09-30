from django.contrib.auth import forms
from typing import Any

User: Any

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model: Any = ...

class UserCreationForm(forms.UserCreationForm):
    error_message: Any = ...
    class Meta(forms.UserCreationForm.Meta):
        model: Any = ...
    def clean_username(self): ...
