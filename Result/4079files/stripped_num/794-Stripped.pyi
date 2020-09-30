# (generated with --quick)

from typing import Any

class ShowroomDownloadError(ShowroomException):
    process: Any
    def __init__(self, process = ...) -> None: ...

class ShowroomException(Exception): ...

class ShowroomStopRequest(ShowroomException): ...
