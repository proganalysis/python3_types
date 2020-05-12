from typing import Any

__author__: Any
__license__: str

def _regex_span(_regex: Any, _str: Any, case_insensitive: bool = ...) -> None: ...
def _sentence_context(match: Any, language: str = ..., case_insensitive: bool = ...): ...
def _paragraph_context(match: Any): ...
def _window_match(match: Any, window: int = ...): ...
def match_regex(input_str: Any, pattern: Any, language: Any, context: Any, case_insensitive: bool = ...) -> None: ...
def search_corpus(pattern: Any, corpus: Any, context: Any, case_insensitive: bool = ..., expand_keyword: bool = ..., lemmatized: bool = ..., threshold: float = ...) -> None: ...
def _keyword_expander(word: Any, language: Any, lemmatized: bool = ..., threshold: float = ...): ...
