from lib import results


def solve(input):
    initial = [int(x) for x in input.split(',')]

    cohorts = [0] * 9
    for i in initial:
        cohorts[i] += 1

    p1 = None
    p2 = None

    for day in range(256):
        new_gen, day_sixers = cohorts[0], cohorts[0]
        for c in range(8):
            cohorts[c] = cohorts[c + 1]
        cohorts[6] += day_sixers
        cohorts[8] = new_gen
        if day == 79:
            p1 = sum(cohorts)

    p2 = sum(cohorts)

    return (p1, p2)


if __name__ == '__main__':
    assert solve("3,4,3,1,2") == (5934, 26984457539)

    input = open("input/day06.txt").read().rstrip()
    (p1, p2) = solve(input)
    results(6, p1, p2)
