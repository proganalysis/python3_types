# (generated with --quick)

from typing import Any, Dict, List

EntityExtractor: Any
Message: Any
Metadata: Any
RasaNLUModelConfig: Any
TrainingData: Any
os: module
utils: Any
warnings: module
write_json_to_file: Any

class EntitySynonymMapper(Any):
    provides: List[str]
    synonyms: Any
    def __init__(self, component_config = ..., synonyms = ...) -> None: ...
    def add_entities_if_synonyms(self, entity_a, entity_b) -> None: ...
    @classmethod
    def load(cls, meta, model_dir = ..., model_metadata = ..., cached_component = ..., **kwargs) -> Any: ...
    def persist(self, file_name, model_dir) -> Dict[str, Any]: ...
    def process(self, message, **kwargs) -> None: ...
    def replace_synonyms(self, entities) -> None: ...
    def train(self, training_data, config, **kwargs) -> None: ...
