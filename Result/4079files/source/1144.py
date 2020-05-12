import os
from dataclasses import dataclass, field
from typing import Any, Dict, List, Mapping

import yaml

def _env_var_constructor(loader: yaml.Loader, node:yaml.Node):
    """Impliments a custom YAML tag for loading optional environment variables.
    If the environment variable is set it returns its value. 
    Otherwise returns `None`.

    Example usage:
        key: !ENV 'KEY'
    """
    if node.id == 'scalar':
        value = loader.construct_scalar(node)
        key = str(value)

    else:
        raise TypeError('Expected a string')

    return os.getenv(key)

yaml.add_constructor(u'!ENV', _env_var_constructor)

@dataclass(init=False, repr=False)
class Config(yaml.YAMLObject):
    yaml_tag = u'!Config'

    def __init__(self, **kwargs):
        for name, value in kwargs:
            setattr(self, name, value)

with open("config-default.yml", encoding="UTF-8") as f:
    BOT_CONFIG = yaml.load(f) # type: Config


