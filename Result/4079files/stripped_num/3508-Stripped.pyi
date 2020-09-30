# (generated with --quick)

from typing import Any, Dict, Optional

_: int
item: int
left_elements: Dict[int, int]
num: int
root: BinaryTree

class BinaryTree(object):
    head: Optional[Node]
    def add(self, node, val) -> None: ...
    def insert(self, item) -> None: ...

class Node(object):
    data: Any
    left: None
    right: None
    def __init__(self, val) -> None: ...

def preorder(hash_map, level, head) -> None: ...
