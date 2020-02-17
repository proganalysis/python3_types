# (generated with --quick)

from typing import Any

ARRAY: Any
BoardModel: Any
BoardModeratorOrmModel: Any
BoardOrmModel: Any
ModeratorModel: Any
PostModel: Any
PostOrmModel: Any
ReportModel: Any
ReportOrmModel: Any
String: Any
ThreadOrmModel: Any
cast: Any
desc: Any
has_role: Any
joinedload: Any
required_roles_for_viewing_reports: Any
roles: Any
session: Any

def create(report) -> Any: ...
def delete(report) -> None: ...
def find_by_id(report_id: int) -> Any: ...
def find_by_moderator(moderator, page: int, per_page: int, for_boards: list) -> list: ...
def find_by_post(post) -> Any: ...
def increase_report_count(report) -> None: ...
