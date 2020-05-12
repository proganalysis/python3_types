from collections import namedtuple
from typing import Any

PracticeOverview = namedtuple('PracticeOverview', ['level', 'mission', 'phase', 'credits', 'tasks', 'skills', 'recommendation'])

StudentTask = namedtuple('StudentTask', ['name', 'attempted', 'solved', 'time'])

StudentSkill = namedtuple('StudentSkill', ['name', 'value'])

def get_tasks(domain: Any, student: Any): ...
def get_skill_list(domain: Any, student: Any): ...
def get_practice_overview(domain: Any, student: Any): ...
