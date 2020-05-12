import json
from pathlib import Path
from rlbot.matchconfig.match_config import MatchConfig, PlayerConfig
from rlbot.parsing.bot_config_bundle import BotConfigBundle as BotConfigBundle
from rlbot.parsing.custom_config import ConfigObject as ConfigObject
from rlbot.parsing.incrementing_integer import IncrementingInteger
from typing import Any

def read_match_config_from_file(match_config_path: Path) -> MatchConfig: ...
def parse_match_config(config_parser: ConfigObject, config_location: Any, config_bundle_overrides: Any, looks_config_overrides: Any) -> MatchConfig: ...
def get_team(config: Any, index: Any): ...
def get_bot_options(bot_type: Any): ...
def _load_bot_config(index: Any, config_bundle: BotConfigBundle, looks_config_object: ConfigObject, overall_config: ConfigObject, human_index_tracker: IncrementingInteger) -> PlayerConfig: ...

known_types: Any

class ConfigJsonEncoder(json.JSONEncoder):
    def default(self, obj: Any): ...

def as_match_config(json_obj: Any) -> MatchConfig: ...
