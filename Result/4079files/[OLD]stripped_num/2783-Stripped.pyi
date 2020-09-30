# (generated with --quick)

import configparser
from typing import Any, Dict, List, Type

CHARACTER_COLLECTION: Any
ConfigParser: Type[configparser.ConfigParser]
Historical: Any
ModelMixin: Any
datetime: Type[datetime.datetime]

class Character(Any, Any):
    DB_COLUMNS: List[str]
    aap: Any
    ap: Any
    char_class: Any
    char_name: Any
    dp: Any
    fam_name: Any
    fame: Any
    gear_pic: Any
    gear_score: Any
    hist_data: Any
    level: Any
    member: Any
    meta: Dict[str, Any]
    objects: Any
    primary: Any
    primary_chars: Any
    progress: Any
    rank: Any
    renown_score: Any
    server: Any
    updated: Any

def __getattr__(name) -> Any: ...
