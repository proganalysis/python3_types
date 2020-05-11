# (generated with --quick)

import json.encoder
import pathlib
from typing import Any, Dict, Tuple, Type

BotConfigBundle: Any
ConfigObject: Any
EXTENSION_PATH_KEY: Any
ExtensionConfig: Any
IncrementingInteger: Any
LoadoutConfig: Any
LoadoutPaintConfig: Any
MatchConfig: Any
MutatorConfig: Any
PARTICIPANT_BOT_SKILL_KEY: Any
PARTICIPANT_CONFIGURATION_HEADER: Any
PARTICIPANT_TEAM: Any
PARTICIPANT_TYPE_KEY: Any
Path: Type[pathlib.Path]
PlayerConfig: Any
RLBOT_CONFIGURATION_HEADER: Any
create_bot_config_layout: Any
get_bot_config_bundles: Any
get_num_players: Any
json: module
known_types: Dict[Any, str]
load_bot_appearance: Any
parse_match_settings: Any

class ConfigJsonEncoder(json.encoder.JSONEncoder):
    def default(self, obj) -> Any: ...

def _load_bot_config(index, config_bundle, looks_config_object, overall_config, human_index_tracker) -> Any: ...
def as_match_config(json_obj) -> Any: ...
def get_bot_options(bot_type) -> Tuple[bool, bool]: ...
def get_team(config, index) -> Any: ...
def parse_match_config(config_parser, config_location, config_bundle_overrides, looks_config_overrides) -> Any: ...
def read_match_config_from_file(match_config_path) -> Any: ...
