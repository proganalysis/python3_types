# (generated with --quick)

from typing import Any, Generator, Iterator, Tuple

Faculty: Any
ModelForm: Any
RegexValidator: Any
StudentInformation: Any
User: Any
UserCreationForm: Any
UserInformation: Any
ValidationError: Any
_: Any
forms: Any
html_clean: Any
name_validator: Any
s_number_validator: Any
validate_email: Any

class AbstractContactForm(Any):
    content: Any
    subject: Any
    def clean(self) -> None: ...

class ContactForm(AbstractContactForm):
    sender: Any

class PrivacyAgreementForm(Any):
    Meta: type

class StudentInformationForm(Any):
    Meta: type

class StudentVerificationForm(Any):
    Meta: type

class UserEditForm(Any):
    Meta: type

class UserForm(Any):
    Meta: type

class UserInformationForm(Any):
    Meta: type
    description: Any

def faculties_or_empty() -> Generator[Tuple[str, str], Any, None]: ...
def get_faculties() -> Iterator: ...
def s_number_existence_validator(number) -> None: ...
def username_existence_validator(number) -> None: ...
