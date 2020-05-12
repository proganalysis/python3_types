from aoareader.Dict import Dict as Vocabulary
from sys import argv as argv
from typing import Any

data_path: str
data_filenames: Any
vocab_file: Any
dict_file: Any

def tokenize(sentence: Any): ...
def parse_stories(lines: Any, with_answer: bool = ...): ...
def get_stories(story_lines: Any, with_answer: bool = ...): ...
def vectorize_stories(stories: Any, vocab: Vocabulary) -> Any: ...
def build_dict(stories: Any): ...
def main() -> None: ...
