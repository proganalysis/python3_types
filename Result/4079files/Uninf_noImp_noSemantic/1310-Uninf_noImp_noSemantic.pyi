from typing import Any, Tuple

LPAR: Any
RPAR: Any
LBRACK: Any
RBRACK: Any
COMMA: Any
EQ: Any
qualifier: Any

def turn_parseresults_to_list(s: Any, loc: Any, toks: Any): ...
def normalise_templates(toks: Any): ...

angle_bracket_pair: Any
parentheses_pair: Any
square_bracket_pair: Any
input_type: Any
number: Any
input_name: Any
pointer_or_reference: Any
default_value: Any
argument_type: Any
argument: Any
arglist: Any

def normalise(symbol: str) -> Tuple[str, str]: ...
