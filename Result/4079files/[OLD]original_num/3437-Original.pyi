# (generated with --quick)

import datasets
import guesser
from typing import Any, Type, Union

ElasticSearchGuesser: Type[guesser.ElasticSearchGuesser]
QB_QUESTION_DB: str
QbApi: Any
QuizBowlDataset: Type[datasets.QuizBowlDataset]
api_key: str
base_url: str
get_word: Any
np: module
os: module
qb_host: str
retry: Any
server: Any
submit_answer: Any
sys: module
time: module
user_id: Union[int, str]

class ThresholdBuzzer:
    threshold: Any
    def __init__(self, threshold = ...) -> None: ...
    def buzz(self, guesses, position) -> Any: ...
    def normalize(self, scores) -> list: ...

def main() -> None: ...
