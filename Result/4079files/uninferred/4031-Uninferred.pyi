from collections import namedtuple

NFA = namedtuple('NFA', ['state', 'groups_count', 'named_groups'])

def to_nfa(expression: str) -> NFA: ...
def to_rpn(expression: str) -> str: ...
def to_atoms(expression: str) -> str: ...

# Names in __all__ with no definition:
#   NFA
