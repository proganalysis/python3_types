import yaml
from dataclasses import field as field
from typing import Any

def _env_var_constructor(loader: yaml.Loader, node: yaml.Node) -> Any: ...

class Config(yaml.YAMLObject):
    yaml_tag: str = ...
    def __init__(self, **kwargs: Any) -> None: ...

BOT_CONFIG: Config
