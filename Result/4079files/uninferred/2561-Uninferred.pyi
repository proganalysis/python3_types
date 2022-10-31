from projects.project_models import Project as Project
from projects.source_models import FileSource, LinkedSourceAuthentication as LinkedSourceAuthentication
from typing import Any

class ProjectFileRefresher:
    project: Project
    target_directory: str
    authentication: LinkedSourceAuthentication
    def __init__(self, project: Project, target_directory: str, authentication: LinkedSourceAuthentication) -> None: ...
    def refresh(self) -> None: ...
    def update_existing_file_sources(self, full_disk_file_path: str, relative_disk_file_path: str) -> bool: ...
    @staticmethod
    def update_source_from_disk(existing_source: FileSource, full_disk_file_path: str) -> Any: ...