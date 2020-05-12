from django.db import models
from typing import Any

User: Any
ProblemAttachmentStorage: Any

class Problem(models.Model):
    title: Any = ...
    categories: Any = ...
    author: Any = ...
    description: Any = ...
    auth_key: Any = ...
    last_modified: Any = ...
    class Meta:
        verbose_name: str = ...
        verbose_name_plural: str = ...
    def categories_title(self): ...
    def __str__(self): ...

class ProblemList(models.Model):
    title: Any = ...
    description: Any = ...
    announcement: Any = ...
    allow_question: Any = ...
    session: Any = ...
    class Meta:
        verbose_name: str = ...
        verbose_name_plural: str = ...
    def __str__(self): ...

def upload_target(problem_attachment: Any, filename: Any): ...

class ProblemAttachment(models.Model):
    file: Any = ...
    problem: Any = ...
    class Meta:
        verbose_name: str = ...
        verbose_name_plural: str = ...
    def filename(self): ...
    def __str__(self): ...

class ProblemInstance(models.Model):
    problem: Any = ...
    problem_list: Any = ...
    points: Any = ...
    distributed_points: Any = ...
    breakthrough_points: Any = ...
    hidden: Any = ...
    class Meta:
        verbose_name: str = ...
        verbose_name_plural: str = ...
    def __str__(self): ...

class ProblemAuthLog(models.Model):
    user: Any = ...
    problem_instance: Any = ...
    auth_key: Any = ...
    datetime: Any = ...
    class Meta:
        unique_together: Any = ...
        verbose_name: str = ...
        verbose_name_plural: str = ...

class ProblemQuestion(models.Model):
    user: Any = ...
    problem_instance: Any = ...
    question: Any = ...
    answer: Any = ...
    datetime: Any = ...
    class Meta:
        verbose_name: str = ...
        verbose_name_plural: str = ...
