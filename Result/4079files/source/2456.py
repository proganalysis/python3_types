import sys
from typing import Dict, FrozenSet, List

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

itemNameToId: Dict[str,int]= {}
itemIdToName: Dict[int,str] = {}


def item_id(name) -> int:
    if not isinstance(name, str):
        raise TypeError("Item name must be string")
    if name not in itemNameToId:
        itemId = len(itemNameToId) + 1
        itemNameToId[name] = itemId
        itemIdToName[itemId] = name
        return itemId
    else:
        return itemNameToId[name]

def item_str(id) -> str:
    return itemIdToName[id]

def ItemSet(lst: List[str]) -> FrozenSet[int]:
    return frozenset(map(item_id, lst))
