# (generated with --quick)

import collections
from typing import Any, Dict, NoReturn, Tuple, Type, Union
import werkzeug.wrappers

F: Any
LIMITS: bool
datetime: Type[datetime.datetime]
db: Any
defaultdict: Type[collections.defaultdict]
json: module
unidecode: Any

class Query(Any):
    created_on: Any
    id: Any
    question_id: Any
    updated_on: Any
    user_id: Any
    word_id: Any

class Question(Any):
    answer: Any
    created_on: Any
    fold: Any
    id: Any
    n_words: Any
    qb_id: Any
    updated_on: Any
    words: Any
    @staticmethod
    def id_translations() -> dict: ...

class QuestionStatus(Any):
    created_on: Any
    position: Any
    question_id: Any
    updated_on: Any
    user_id: Any
    word_id: Any

class QuizBowl:
    @staticmethod
    def check_auth(user_id, api_key) -> Any: ...
    @staticmethod
    def create_user(email, api_key) -> Dict[str, Any]: ...
    @staticmethod
    def get_buzzes() -> Dict[Tuple[Any, Any], Tuple[Any, Any]]: ...
    @staticmethod
    def get_scores() -> Dict[Any, Tuple[Any, Any]]: ...
    @staticmethod
    def handle_word_request(user_id, question_id, position) -> Dict[str, Any]: ...
    @staticmethod
    def list_questions() -> Dict[str, list]: ...
    @staticmethod
    def num_questions(fold = ...) -> Any: ...
    @staticmethod
    def question_length(question_id) -> Any: ...
    @staticmethod
    def question_statuses(user_id) -> Any: ...
    @staticmethod
    def submit_guess(user_id, question_id, guess) -> Tuple[Any, bool]: ...
    @staticmethod
    def user_answer_pairs() -> Any: ...

class Result(Any):
    correct: Any
    created_on: Any
    fold: Any
    guess: Any
    position: Any
    question_id: Any
    updated_on: Any
    user_id: Any
    word_id: Any

class User(Any):
    api_key: Any
    created_on: Any
    display_name: Any
    email: Any
    id: Any
    queries: Any
    question_statuses: Any
    updated_on: Any

class Word(Any):
    created_on: Any
    id: Any
    position: Any
    question_id: Any
    text: Any
    updated_on: Any

def abort(status: Union[int, werkzeug.wrappers.Response], *args, **kwargs) -> NoReturn: ...
def load_questions(filename = ...) -> None: ...
