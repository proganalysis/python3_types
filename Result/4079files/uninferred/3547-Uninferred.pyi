from typing import Any

class MacIntyreContractions:
    CONTRACTIONS2: Any = ...
    CONTRACTIONS3: Any = ...
    CONTRACTIONS4: Any = ...

class TreebankWordTokenizer:
    STARTING_QUOTES: Any = ...
    PUNCTUATION: Any = ...
    PARENS_BRACKETS: Any = ...
    CONVERT_PARENTHESES: Any = ...
    DOUBLE_DASHES: Any = ...
    ENDING_QUOTES: Any = ...
    _contractions: Any = ...
    CONTRACTIONS2: Any = ...
    CONTRACTIONS3: Any = ...
    def tokenize(self, text: Any, convert_parentheses: bool = ..., return_str: bool = ...): ...

def word_tokenize(text: Any, language: str = ..., preserve_line: bool = ...): ...
