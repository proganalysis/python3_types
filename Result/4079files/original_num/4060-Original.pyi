# (generated with --quick)

from typing import Any, Dict, List, Optional

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
    def __init__(self, component_config: Optional[Dict[str, str]] = ..., synonyms: Optional[Dict[str, Any]] = ...) -> None: ...
    def add_entities_if_synonyms(self, entity_a, entity_b) -> None: ...
    @classmethod
    def load(cls, meta: Dict[str, Any], model_dir: Optional[str] = ..., model_metadata = ..., cached_component: Optional[EntitySynonymMapper] = ..., **kwargs) -> EntitySynonymMapper: ...
    def persist(self, file_name: str, model_dir: str) -> Optional[Dict[str, Any]]: ...
    def process(self, message, **kwargs) -> None: ...
    def replace_synonyms(self, entities) -> None: ...
    def train(self, training_data, config, **kwargs) -> None: ...
