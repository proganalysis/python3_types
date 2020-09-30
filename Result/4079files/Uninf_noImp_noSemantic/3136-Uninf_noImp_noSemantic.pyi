from collections import namedtuple
from typing import Any

host: str

CachedBeatmap = namedtuple('CachedBeatmap', 'url_or_id beatmap')

PPStats = namedtuple('PPStats', 'pp stars artist title version')

ClosestPPStats = namedtuple('ClosestPPStats', 'acc pp stars artist title version')
plugin_path: str
beatmap_path: Any
cached_beatmap: Any

async def is_osu_file(url: str) -> Any: ...
async def download_beatmap(beatmap_url_or_id: Any) -> None: ...
async def parse_map(beatmap_url_or_id: Any): ...
def apply_settings(beatmap: Any, args: Any): ...
async def calculate_pp(beatmap_url_or_id: Any, *options: Any): ...
