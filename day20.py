from lib import results


def build_image(lines):
    w = len(lines[0])
    image = set()
    for i, v in enumerate(''.join(lines)):
        if v == '#':
            image.add((i % w, i // w))
    return image


adjacents = [(-1, -1), (0, -1), (1, -1), (-1, 0),
             (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def print_image(image, inverted, sx, sy, w, h):
    s_image = ""
    for y in range(sy, sy + h):
        line = ""
        for x in range(sx, sx + w):
            if inverted:
                line += " " if (x, y) in image else "#"
            else:
                line += "#" if (x, y) in image else " "
        s_image += line + "\n"
    print(s_image)


def enhance(image, algo, inverted, should_flip_flop):
    next_image = set()

    minx, miny, maxx, maxy = 100000, 100000, -100000, -100000
    for (x, y) in image:
        if x < minx:
            minx = x
        if y < miny:
            miny = y
        if x > maxx:
            maxx = x
        if y > maxy:
            maxy = y

    next_inverted = not inverted if should_flip_flop else inverted

    for y in range(miny - 1, maxy + 2):
        for x in range(minx - 1, maxx + 2):
            index = 0
            for (dx, dy) in adjacents:
                nx, ny = x + dx, y + dy

                if inverted:
                    a = (0 if (nx, ny) in image else 1)

                    index = (index << 1) + a
                else:
                    a = (1 if (nx, ny) in image else 0)

                    index = (index << 1) + a
            if inverted:
                if should_flip_flop and algo[index] == '#':
                    next_image.add((x, y))
                elif not should_flip_flop and algo[index] == '.':
                    next_image.add((x, y))
            else:
                if should_flip_flop and algo[index] == '.':
                    next_image.add((x, y))
                elif not should_flip_flop and algo[index] == '#':
                    next_image.add((x, y))

    return next_image, next_inverted


def solve(input):
    lines = input.splitlines()
    algo = lines[0]
    image = build_image(lines[2:])

    should_flip_flop = algo[0] == '#'
    inverted = False

    p1 = None
    p2 = None
    for i in range(50):
        image, inverted = enhance(image, algo, inverted, should_flip_flop)
        if i == 1:
            p1 = len(image)
        if i == 49:
            p2 = len(image)

    return (p1, p2)


if __name__ == '__main__':
    assert solve('''..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###''') == (35, 3351)

    input = open("input/day20.txt").read().rstrip()
    (p1, p2) = solve(input)
    results(20, p1, p2)
