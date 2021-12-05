from lib import results
from collections import Counter


def parse_line(line):
    [a, b] = line.split(" -> ")
    return (tuple(map(int, a.split(','))), tuple(map(int, b.split(','))))


def is_h_or_v(line):
    ((x1, y1), (x2, y2)) = line
    return x1 == x2 or y1 == y2


def plot_line(line_plot, line):
    ((x1, y1), (x2, y2)) = line

    xstep = 1 if x1 < x2 else -1
    ystep = 1 if y1 < y2 else -1

    for x in range(x1, x2 + xstep, xstep):
        for y in range(y1, y2 + ystep, ystep):
            line_plot[(x, y)] += 1


def plot_diag(line_plot, line):
    ((x1, y1), (x2, y2)) = line

    xstep = 1 if x1 < x2 else -1
    ystep = 1 if y1 < y2 else -1

    for point in zip(range(x1, x2 + xstep, xstep), range(y1, y2 + ystep, ystep)):
        line_plot[point] += 1


def solve(input):
    lines = [parse_line(line) for line in input.splitlines()]
    line_plot = Counter()

    for line in lines:
        if is_h_or_v(line):
            plot_line(line_plot, line)

    p1 = 0
    for (_, c) in line_plot.items():
        if c > 1:
            p1 += 1

    for line in lines:
        if not is_h_or_v(line):
            plot_diag(line_plot, line)
    p2 = 0
    for (_, c) in line_plot.items():
        if c > 1:
            p2 += 1

    return (p1, p2)


if __name__ == '__main__':
    assert solve('''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2''') == (5, 12)

    input = open("input/day05.txt").read().rstrip()
    (p1, p2) = solve(input)
    results(5, p1, p2)
