from lib import results


adjacent = [(-1, -1), (0, -1), (1, -1), (1, 0),
            (1, 1), (0, 1), (-1, 1), (-1, 0)]


def print_grid(grid):
    line = ""
    for (i, c) in enumerate(grid):
        line += str(c)
        if (i + 1) % 10 == 0:
            print(line)
            line = ""


def get_coords(i):
    return (i % 10, i // 10)


def get_index(x, y):
    return x + y * 10


def flash(grid, i):
    if grid[i] < 10:
        return
    grid[i] = -1
    (x, y) = get_coords(i)
    for (dx, dy) in adjacent:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx > 9 or ny < 0 or ny > 9:
            continue
        ni = get_index(nx, ny)
        if grid[ni] > -1:
            grid[ni] += 1
            if grid[ni] > 9:
                flash(grid, ni)


def step(grid):
    will_flash = []

    for i in range(len(grid)):
        grid[i] += 1
        if grid[i] > 9:
            will_flash.append(i)

    for i in will_flash:
        flash(grid, i)

    flash_count = 0

    insync = True
    for i in range(len(grid)):
        if grid[i] == -1:
            grid[i] = 0
            flash_count += 1
        else:
            insync = False

    return (flash_count, insync)


def solve(input):
    grid = [int(x) for x in ''.join(input.splitlines())]

    p1 = 0

    for _ in range(100):
        (flashes, insync) = step(grid)
        p1 += flashes

    done = False
    p2 = 100
    while not done:
        (_, insync) = step(grid)
        done = insync
        p2 += 1

    return (p1, p2)


if __name__ == '__main__':
    assert solve('''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526''') == (1656, 195)

    input = open("input/day11.txt").read().rstrip()
    (p1, p2) = solve(input)
    results(11, p1, p2)
