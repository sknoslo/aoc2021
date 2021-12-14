from lib import results
from itertools import pairwise
from collections import Counter


def solve(puzzle_input):
    lines = puzzle_input.splitlines()

    template = lines[0]

    rules = dict([tuple(x.split(' -> ')) for x in lines[2:]])

    polymer = template

    for _ in range(10):
        polymer_next = polymer[0]
        for (a, b) in pairwise(polymer):
            key = a + b
            if key in rules:
                middle = rules[key]
                polymer_next += middle + b
        polymer = polymer_next

    counts = Counter(polymer).values()

    p1 = max(counts) - min(counts)

    expand_memo = dict()

    def expand(rules, key, times):
        if (key, times) in expand_memo:
            return expand_memo[(key, times)]
        middle = rules[key]

        if times == 1:
            return Counter(key + middle)

        res = expand(rules, key[0] + middle, times - 1) + \
            expand(rules, middle + key[1], times - 1)
        res[middle] -= 1
        expand_memo[(key, times)] = res
        return res

    counter = Counter()

    pairs = list(pairwise(template))
    for (i, (a, b)) in enumerate(pairs):
        key = a + b
        counter += expand(rules, key, 40)
        if i < len(pairs) - 1:
            counter[b] -= 1

    counts = counter.values()
    p2 = max(counts) - min(counts)

    return (p1, p2)


if __name__ == '__main__':
    assert solve('''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C''') == (1588, 2188189693529)

    puzzle_input = open("input/day14.txt").read().rstrip()
    (p1, p2) = solve(puzzle_input)
    results(14, p1, p2)
