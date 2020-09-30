# (generated with --quick)

from typing import Any, List

csv: module
json: module
os: module
re: module
subprocess: module

class CommentBucket(object):
    comments: list
    fieldnames: List[str]
    video_id: Any
    def __init__(self, video_id) -> None: ...
    def _clear(self) -> None: ...
    def _format(self, comments, filtered_comments) -> None: ...
    def fetch_all_comments(self) -> list: ...
    def get_csv(self) -> None: ...
    def get_json(self) -> None: ...
