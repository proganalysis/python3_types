# (generated with --quick)

from typing import Any, Pattern

_episode_info_re: Pattern[str]
_week_re: Pattern[str]
episode_list_path: str
episode_list_url: str
glob: module
iso_date_to_six_char: Any
json: module
os: module
re: module
trim: Any

def get_trim_pts(srcpath) -> Any: ...
def kimi_dare_dispatch(**kwargs) -> None: ...
def load_episode_list() -> Any: ...
def trim_episodes(work_dir, dest_dir, data) -> None: ...
def update_episode_list(data) -> None: ...
