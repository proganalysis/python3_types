# (generated with --quick)

from typing import Any, List, Pattern, Tuple, Union

__all__: List[str]
_treebank_word_tokenizer: TreebankWordTokenizer
re: module
sent_tokenize: Any

class MacIntyreContractions:
    CONTRACTIONS2: List[str]
    CONTRACTIONS3: List[str]
    CONTRACTIONS4: List[str]
    __doc__: str

class TreebankWordTokenizer:
    CONTRACTIONS2: List[Pattern[nothing]]
    CONTRACTIONS3: List[Pattern[nothing]]
    CONVERT_PARENTHESES: List[Tuple[Pattern[str], str]]
    DOUBLE_DASHES: Tuple[Pattern[str], str]
    ENDING_QUOTES: List[Tuple[Pattern[str], str]]
    PARENS_BRACKETS: Tuple[Pattern[str], str]
    PUNCTUATION: List[Tuple[Pattern[str], str]]
    STARTING_QUOTES: List[Tuple[Pattern[str], str]]
    __doc__: str
    _contractions: MacIntyreContractions
    def tokenize(self, text, convert_parentheses = ..., return_str = ...) -> Union[str, List[str]]: ...

def word_tokenize(text, language = ..., preserve_line = ...) -> list: ...
