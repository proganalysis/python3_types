# (generated with --quick)

from typing import Any, List, Tuple

_: Any
models: Any
os: module
timesince: Any
uuid: module

class Custodian(Any):
    CATEGORIES: List[Tuple[str, Any]]
    Meta: type
    __doc__: str
    authorized_signature: Any
    category: Any
    emergency_contact: Any
    minor: Any
    person: Any
    def __str__(self) -> str: ...

class Enrolment(Any):
    Meta: type
    created: Any
    group: Any
    person: Any

class Event(Any):
    Meta: type
    comment: Any
    event_end: Any
    event_name: Any
    event_start: Any

class Group(Any):
    Meta: type
    group_name: Any
    project: Any
    def __str__(self) -> str: ...

class Member(Any):
    CATEGORY: List[Tuple[str, Any]]
    Meta: type
    __doc__: str
    bursary: Any
    card_status: Any
    category: Any
    documentation_correct: bool
    dpa_status: Any
    id_card_status: Any
    membership: Any
    person: Any
    photo: Any
    photo_status: Any
    ss_card_status: Any
    def __str__(self) -> str: ...

class Membership(Any):
    Meta: type
    __doc__: str
    id: Any
    membership_fee: Any
    membership_status: Any
    payment_status: Any
    type_of_membership: Any

class Person(Any):
    Meta: type
    address_country: Any
    address_locality: Any
    address_region: Any
    address_street: Any
    age: Any
    birthday: Any
    comment: Any
    dpa_authorization: Any
    email: Any
    health_warnings: Any
    id: Any
    id_number: Any
    id_photocopy: Any
    mobile_number: Any
    name: Any
    phone_number: Any
    photo: Any
    postal_code: Any
    ss_number: Any
    ss_photocopy: Any
    surname: Any
    def __str__(self) -> str: ...

class Project(Any):
    Meta: type
    comment: Any
    date_end: Any
    date_start: Any
    project_name: Any
    def __str__(self) -> str: ...

class Recipient(Any):
    CATEGORIES: List[Tuple[str, Any]]
    COURSES: List[Tuple[str, Any]]
    Meta: type
    __doc__: str
    authorize_photo: Any
    category: Any
    courses: Any
    person: Any
    school: Any
    sibling: Any
    def __str__(self) -> str: ...

class Volunteer(Any):
    Meta: type
    __doc__: str
    comment: Any
    lack_of_sexual_offenses_date_certificate: Any
    person: Any
    def __str__(self) -> str: ...

def _get_file_path(instance, filename) -> str: ...
