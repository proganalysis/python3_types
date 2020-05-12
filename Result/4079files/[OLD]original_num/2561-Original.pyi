# (generated with --quick)

from typing import Any

DirectoryEntryType: Any
File: Any
FileSource: Any
LinkedSourceAuthentication: Any
Project: Any
generate_project_storage_directory: Any
os: module
recursive_directory_list: Any
strip_directory: Any
to_utf8: Any
utf8_path_join: Any

class ProjectFileRefresher(object):
    __doc__: str
    authentication: Any
    project: Any
    target_directory: str
    def __init__(self, project, target_directory: str, authentication) -> None: ...
    def refresh(self) -> None: ...
    def update_existing_file_sources(self, full_disk_file_path: str, relative_disk_file_path: str) -> bool: ...
    @staticmethod
    def update_source_from_disk(existing_source, full_disk_file_path: str) -> None: ...
