from lib import results
from more_itertools import windowed


def count_increases(distances):
    prev = None
    increases = 0
    for distance in distances:
        if prev != None and distance > prev:
            increases += 1
        prev = distance
    return increases


def solve(input):
    distances = list(map(int, input.splitlines(False)))

    p1 = count_increases(distances)

    summed = list(map(sum, windowed(distances, 3)))

    p2 = count_increases(summed)

    return (p1, p2)


if __name__ == '__main__':
    sample = '''199
200
208
210
200
207
240
269
260
263'''
    assert solve(sample) == (7, 5)

    input = open("input/day01.txt").read().rstrip()
    (p1, p2) = solve(input)
    results(1, p1, p2)
