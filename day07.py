from lib import results
from sys import maxsize

cost_memo = dict()


def cost(a, b):
    diff = abs(a-b)
    if not cost_memo.get(diff):
        c = 0
        for i in range(1, diff + 1):
            c += i
        cost_memo[diff] = c
    return cost_memo[diff]


def solve(input):
    crabs = [int(x) for x in input.split(',')]

    low, high = min(crabs), max(crabs)

    p1_min_fuel = maxsize
    p2_min_fuel = maxsize
    for d in range(low, high + 1):
        p1_fuel = 0
        p2_fuel = 0
        for c in crabs:
            p1_fuel += abs(c - d)
            p2_fuel += cost(c, d)
        p1_min_fuel = min(p1_fuel, p1_min_fuel)
        p2_min_fuel = min(p2_fuel, p2_min_fuel)

    return (p1_min_fuel, p2_min_fuel)


if __name__ == '__main__':
    assert solve("16,1,2,0,4,2,7,1,2,14") == (37, 168)

    input = open("input/day07.txt").read().rstrip()
    (p1, p2) = solve(input)
    results(7, p1, p2)
