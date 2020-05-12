from django.db import models
from typing import Any

def _get_file_path(instance: Any, filename: Any): ...

class Person(models.Model):
    class Meta:
        verbose_name: Any = ...
    id: Any = ...
    name: Any = ...
    surname: Any = ...
    birthday: Any = ...
    id_number: Any = ...
    id_photocopy: Any = ...
    ss_number: Any = ...
    ss_photocopy: Any = ...
    postal_code: Any = ...
    address_street: Any = ...
    address_locality: Any = ...
    address_region: Any = ...
    address_country: Any = ...
    phone_number: Any = ...
    mobile_number: Any = ...
    email: Any = ...
    dpa_authorization: Any = ...
    comment: Any = ...
    health_warnings: Any = ...
    photo: Any = ...
    @property
    def age(self): ...
    def __str__(self): ...

class Recipient(models.Model):
    class Meta:
        verbose_name: Any = ...
    CATEGORIES: Any = ...
    COURSES: Any = ...
    courses: Any = ...
    school: Any = ...
    sibling: Any = ...
    authorize_photo: Any = ...
    category: Any = ...
    person: Any = ...
    def __str__(self): ...

class Volunteer(models.Model):
    class Meta:
        verbose_name: Any = ...
    lack_of_sexual_offenses_date_certificate: Any = ...
    comment: Any = ...
    person: Any = ...
    def __str__(self): ...

class Custodian(models.Model):
    class Meta:
        verbose_name: Any = ...
    authorized_signature: Any = ...
    emergency_contact: Any = ...
    CATEGORIES: Any = ...
    category: Any = ...
    person: Any = ...
    minor: Any = ...
    def __str__(self): ...

class Project(models.Model):
    class Meta:
        verbose_name: Any = ...
    project_name: Any = ...
    date_start: Any = ...
    date_end: Any = ...
    comment: Any = ...
    def __str__(self): ...

class Group(models.Model):
    class Meta:
        verbose_name: Any = ...
    group_name: Any = ...
    project: Any = ...
    def __str__(self): ...

class Event(models.Model):
    class Meta:
        verbose_name: Any = ...
    event_name: Any = ...
    event_start: Any = ...
    event_end: Any = ...
    comment: Any = ...

class Enrolment(models.Model):
    class Meta:
        verbose_name: Any = ...
        verbose_name_plural: Any = ...
        unique_together: Any = ...
    person: Any = ...
    group: Any = ...
    created: Any = ...

class Membership(models.Model):
    class Meta:
        verbose_name: Any = ...
    id: Any = ...
    type_of_membership: Any = ...
    payment_status: Any = ...
    membership_fee: Any = ...
    membership_status: Any = ...

class Member(models.Model):
    class Meta:
        verbose_name: Any = ...
    CATEGORY: Any = ...
    category: Any = ...
    id_card_status: Any = ...
    ss_card_status: Any = ...
    photo_status: Any = ...
    dpa_status: Any = ...
    card_status: Any = ...
    bursary: Any = ...
    photo: Any = ...
    person: Any = ...
    membership: Any = ...
    @property
    def documentation_correct(self): ...
    def __str__(self): ...
