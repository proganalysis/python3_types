# (generated with --quick)

from typing import Any

BooleanField: Any
Email: Any
EqualTo: Any
Form: Any
Length: Any
PasswordField: Any
Regexp: Any
Required: Any
StringField: Any
SubmitField: Any
ValidationError: Any
models: Any

class LoginForm(Any):
    email: Any
    password: Any
    remember_me: Any
    submit: Any

class RegistrationForm(Any):
    email: Any
    password: Any
    password2: Any
    submit: Any
    def validate_email(self, field) -> None: ...
