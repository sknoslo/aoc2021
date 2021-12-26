from lib import results


def solve(input):
    lines = input.splitlines()
    h = len(lines)
    w = len(lines[0])
    cells = [c for c in ''.join(lines)]

    def i(x, y):
        return (y % h) * w + (x % w)

    keepgoing = True
    steps = 0
    while keepgoing:
        keepgoing = False
        steps += 1
        next_cells = cells.copy()
        for y in range(h):
            for x in range(w):
                if cells[i(x, y)] == '>' and cells[i(x + 1, y)] == '.':
                    keepgoing = True
                    next_cells[i(x, y)] = '.'
                    next_cells[i(x + 1, y)] = '>'
        cells = next_cells
        next_cells = cells.copy()
        for x in range(w):
            for y in range(h):
                if cells[i(x, y)] == 'v' and cells[i(x, y + 1)] == '.':
                    keepgoing = True
                    next_cells[i(x, y)] = '.'
                    next_cells[i(x, y + 1)] = 'v'

        cells = next_cells

    return (steps, None)


if __name__ == '__main__':
    assert solve('''v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>''') == (58, None)

    input = open("input/day25.txt").read().rstrip()
    (p1, p2) = solve(input)
    results(25, p1, p2)
