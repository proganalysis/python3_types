from index import InvertedIndex
from apriori import apriori
from item import item_id, item_str, ItemSet
from generaterules import generate_rules
import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")


def test_apriori():
    data = ("a,b,c,d,e,f\n"
            "g,h,i,j,k,l\n"
            "z,x\n"
            "z,x\n"
            "z,x,y\n"
            "z,x,y,i\n")

    expectedItemSets = {ItemSet("i"): 2 / 6,
                        ItemSet("z"): 4 / 6,
                        ItemSet("x"): 4 / 6,
                        ItemSet("y"): 2 / 6,
                        ItemSet("xz"): 4 / 6,
                        ItemSet("yz"): 2 / 6,
                        ItemSet("xy"): 2 / 6,
                        ItemSet("xyz"): 2 / 6}

    index = InvertedIndex()
    index.load(data)
    itemsets = apriori(index, 2 / 6)
    assert(len(itemsets) == len(expectedItemSets))
    for itemset in itemsets:
        assert(frozenset(itemset) in expectedItemSets)
    for itemset in itemsets:
        assert(expectedItemSets[frozenset(itemset)] == index.support(itemset))

    print("Itemsets={}".format([i for i in itemsets if len(i) > 1]))

    def itemize(a):
        return list(map(item_id, a))

    # (antecedent, consequent, confidence, lift, support)
    rx = [
        (['y'], ['x'], 1.0, 1.5, 0.3333333333333333),
        (['x'], ['y'], 0.5, 1.5, 0.3333333333333333),
        (['y'], ['z'], 1.0, 1.5, 0.3333333333333333),
        (['z'], ['y'], 0.5, 1.5, 0.3333333333333333),
        (['x'], ['z'], 1.0, 1.5, 0.6666666666666666),
        (['z'], ['x'], 1.0, 1.5, 0.6666666666666666),
        (['x', 'y'], ['z'], 1.0, 1.5, 0.3333333333333333),
        (['z', 'y'], ['x'], 1.0, 1.5, 0.3333333333333333),
        (['z', 'x'], ['y'], 0.5, 1.5, 0.3333333333333333),
        (['y'], ['z', 'x'], 1.0, 1.5, 0.3333333333333333),
        (['x'], ['z', 'y'], 0.5, 1.5, 0.3333333333333333),
        (['z'], ['x', 'y'], 0.5, 1.5, 0.3333333333333333)
    ]

    expectedRules = list(map(lambda a: (itemize(a[0]), itemize(a[1]), a[2], a[3], a[4]), rx))

    itemset_counts = dict(map(lambda i: (tuple(i), index.count(i)), itemsets))
    rules = generate_rules(
        itemsets,
        itemset_counts,
        index.num_transactions,
        0,
        0)

    def deitemize(a):
        return list(map(item_str, a))

    p = list(map(lambda a: (deitemize(a[0]), deitemize(a[1]), a[2], a[3], a[4]), rules))
    print("rules")
    print(p)

    for (antecedent,
         consequent,
         confidence,
         lift,
         support) in rules:
        print("{}, {} conf={:.4f}, {:.4f}, {:.4f}".
              format(antecedent, consequent, confidence, lift, support))

    assert(len(rules) == len(expectedRules))
    for i in range(len(rules)):
        assert(expectedRules[i] in rules)
