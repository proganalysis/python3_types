# (generated with --quick)

import datetime
from typing import Any, Type

Course: Any
CourseInstance: Any
CourseModule: Any
LearningObjectCategory: Any
StaticExercise: Any
TestCase: Any
User: Any
timedelta: Type[datetime.timedelta]
timezone: Any

class RedirectTest(Any):
    course: Any
    course_instance: Any
    course_module: Any
    exercise: Any
    learning_object_category: Any
    user: Any
    def setUp(self) -> None: ...
    def test_course(self) -> None: ...
    def test_course_instance(self) -> None: ...
    def test_course_instance_exercise(self) -> None: ...
    def test_exercise(self) -> None: ...
