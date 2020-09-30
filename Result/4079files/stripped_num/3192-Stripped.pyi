# (generated with --quick)

from typing import Any, Dict, Type
import uplift_backend.models

BugAnalysis: Type[uplift_backend.models.BugAnalysis]
BugContributor: Type[uplift_backend.models.BugContributor]
BugResult: Type[uplift_backend.models.BugResult]
Contributor: Type[uplift_backend.models.Contributor]
PatchStatus: Type[uplift_backend.models.PatchStatus]
SCOPES_ADMIN: Any
current_user: Any
html: module
log: Any
logger: Any

def serialize_analysis(analysis, bugs_nb, full = ...) -> Dict[str, Any]: ...
def serialize_bug(bug) -> Dict[str, Any]: ...
def serialize_contributor(contributor, link = ...) -> Dict[str, Any]: ...
def serialize_patch(patch) -> Dict[str, Any]: ...
def serialize_patch_status(patch_status) -> Dict[str, Any]: ...
