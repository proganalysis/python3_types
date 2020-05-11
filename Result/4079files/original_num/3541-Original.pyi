# (generated with --quick)

from typing import Any

ACCESS: Any
ApiResourceMixin: Any
CourseInstanceBaseMixin: Any
CourseModuleBaseMixin: Any
ExerciseBaseMixin: Any
Http404: Any
LearningObject: Any
Submission: Any
SubmissionBaseMixin: Any

class ExerciseBaseResourceMixin(Any, Any, Any):
    exercise_kw: str
    def get_course_instance_object(self) -> Any: ...
    def get_course_module_object(self) -> Any: ...
    def get_exercise_object(self) -> Any: ...

class ExerciseResourceMixin(ExerciseBaseResourceMixin, Any):
    access_mode: Any
    def get_access_mode(self) -> Any: ...

class SubmissionBaseResourceMixin(ExerciseBaseResourceMixin, Any):
    submission_kw: str
    def get_submission_object(self) -> Any: ...

class SubmissionResourceMixin(SubmissionBaseResourceMixin, Any):
    access_mode: Any
    def get_access_mode(self) -> Any: ...
