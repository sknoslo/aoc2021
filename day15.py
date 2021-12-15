from lib import results
from heapq import heappop, heappush


def find_path(grid, w, h):
    goal = len(grid) - 1

    def to_i(x, y):
        return x + y * w

    q = []
    heappush(q, (0, (0, 0)))

    seen = set()

    while len(q) > 0:
        (r, (x, y)) = heappop(q)
        if (x, y) in seen:
            continue

        seen.add((x, y))

        i = to_i(x, y)
        if i == goal:
            return r

        for (dx, dy) in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            if nx < w and nx >= 0 and ny < h and ny >= 0:
                nr = grid[to_i(nx, ny)]
                heappush(q, (r + nr, (nx, ny)))
    return 0


def solve(input):
    lines = input.splitlines()

    h = len(lines)
    w = len(lines[0])

    grid = [int(x) for x in ''.join(lines)]

    p1 = find_path(grid, w, h)

    bw = w * 5
    bh = h * 5

    bigger_grid = [0] * (bw * bh)
    for y in range(bh):
        for x in range(bw):
            ox = x % w
            oy = y % h
            mx = x // w
            my = y // h
            risk = grid[ox + oy * w] + mx + my
            risk = risk if risk < 10 else risk % 10 + 1
            bigger_grid[x + y * bw] = risk

    p2 = find_path(bigger_grid, bw, bh)

    return (p1, p2)


if __name__ == '__main__':
    assert solve('''1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581''') == (40, 315)

    input = open("input/day15.txt").read().rstrip()
    (p1, p2) = solve(input)
    results(15, p1, p2)
