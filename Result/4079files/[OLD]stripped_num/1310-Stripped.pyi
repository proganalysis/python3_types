# (generated with --quick)

from typing import Any, Tuple, TypeVar

COMMA: Any
Combine: Any
EQ: Any
Group: Any
LBRACK: Any
LPAR: Any
Literal: Any
OneOrMore: Any
Optional: Any
ParseException: Any
ParseResults: Any
RBRACK: Any
RPAR: Any
SkipTo: Any
Word: Any
alphanums: Any
angle_bracket_pair: Any
arglist: Any
argument: Any
argument_type: Any
default_value: Any
delimitedList: Any
input_name: Any
input_type: Any
nestedExpr: Any
number: Any
nums: Any
oneOf: Any
parentheses_pair: Any
pointer_or_reference: Any
qualifier: Any
quotedString: Any
square_bracket_pair: Any
ungroup: Any

_T0 = TypeVar('_T0')

def normalise(symbol: _T0) -> Tuple[Any, str]: ...
def normalise_templates(toks) -> str: ...
def turn_parseresults_to_list(s, loc, toks) -> Any: ...
