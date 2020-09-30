from rasa.nlu.training_data import TrainingData
from rasa.nlu.training_data.formats.readerwriter import JsonTrainingDataReader
from typing import Any, Dict, Text

logger: Any

class LuisReader(JsonTrainingDataReader):
    def read_from_json(self, js: Dict[Text, Any], **kwargs: Any) -> TrainingData: ...
