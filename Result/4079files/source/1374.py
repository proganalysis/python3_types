from itertools import product
from typing import List
import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")


def contains_all_subsets(candidate, candidates):
    for item in candidate:
        if candidate - {item} not in candidates:
            return False
    return True


def apriori(index, minsup) -> List[List[int]]:
    print("Apriori with minsup={}".format(minsup))
    candidates = set(
        [frozenset({i}) for i in index.items() if index.support({i}) >= minsup])
    results = list(candidates)
    itemset_size = 1
    while len(candidates) > 0:
        generation = set()
        for (a, b) in product(candidates, repeat=2):
            if (len(a - b) == 1
                and index.support(a | b) >= minsup
                    and contains_all_subsets(a | b, candidates)):
                generation.add(frozenset(a | b))
        print(
            "Generated {} itemsets of size {}".format(
                len(generation),
                itemset_size))
        itemset_size += 1
        results.extend(list(generation))
        candidates = generation
    return list(map(lambda x: list(sorted(list(x))), results))
