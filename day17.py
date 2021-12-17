from lib import results


def reaches_target(vx, vy, minx, miny, maxx, maxy):
    x, y = 0, 0
    while x <= maxx and y >= miny:
        x += vx
        y += vy
        vx = max(0, vx - 1)
        vy = vy - 1
        if minx <= x <= maxx and miny <= y <= maxy:
            return True
    return False


def solve(input: str):
    input = input.replace("target area: ", "")
    x, y = input.split(", ")
    x = x[2:]
    y = y[2:]
    minx, maxx = [int(v) for v in x.split("..")]
    miny, maxy = [int(v) for v in y.split("..")]

    initialv = abs(miny) - 1
    p1 = sum([i for i in range(initialv + 1)])

    max_iv_y = abs(miny) - 1
    min_iv_y = miny
    max_iv_x = maxx
    min_iv_x = 0
    acc = 0
    s = 1
    while acc < minx:
        min_iv_x = s
        acc += s
        s += 1

    good = set()

    for vx in range(min_iv_x, max_iv_x + 1):
        for vy in range(min_iv_y, max_iv_y + 1):
            if reaches_target(vx, vy, minx, miny, maxx, maxy):
                good.add((vx, vy))

    p2 = len(good)
    return (p1, p2)


if __name__ == '__main__':
    assert solve("target area: x=20..30, y=-10..-5") == (45, 112)

    input = open("input/day17.txt").read().rstrip()
    (p1, p2) = solve(input)
    results(17, p1, p2)
