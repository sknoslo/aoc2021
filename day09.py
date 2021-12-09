from lib import results
from functools import reduce
from operator import mul


def get_cell(h_map, w, x, y):
    return h_map[x + y * w]


def solve(input):
    lines = input.splitlines()
    w, h = len(lines[0]), len(lines)

    h_map = list(map(int, list(''.join(lines))))

    p1 = 0
    low_spots = []
    for x in range(w):
        for y in range(h):
            neighbors = [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]
            cell = get_cell(h_map, w, x, y)
            lowest = True
            for (nx, ny) in neighbors:
                if nx < w and nx >= 0 and ny < h and ny >= 0:
                    lowest = lowest and cell < get_cell(h_map, w, nx, ny)
            if lowest:
                low_spots.append((x, y))
                p1 += 1 + cell

    basin_sizes = []
    for (x, y) in low_spots:
        # do an exhaustive search, and count all non-9 reachable cells
        size = 0
        seen = set()
        to_visit = [(x, y)]

        while len(to_visit) > 0:
            (x, y) = to_visit.pop()
            if (x, y) in seen or x < 0 or y < 0 or x >= w or y >= h:
                continue
            seen.add((x, y))
            cell = get_cell(h_map, w, x, y)

            if cell != 9:
                size += 1
                neighbors = [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]
                for (nx, ny) in neighbors:
                    to_visit.append((nx, ny))
        basin_sizes.append(size)
    basin_sizes.sort()

    p2 = reduce(mul, basin_sizes[-3:])

    return (p1, p2)


if __name__ == '__main__':
    assert solve('''2199943210
3987894921
9856789892
8767896789
9899965678''') == (15, 1134)

    input = open("input/day09.txt").read().rstrip()
    (p1, p2) = solve(input)
    results(9, p1, p2)
