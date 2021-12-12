from lib import results


def add_path(caves, a, b):
    if a in caves:
        caves[a].append(b)
    else:
        caves[a] = [b]


def solve(input):
    caves = dict()
    for line in input.splitlines():
        [a, b] = line.split('-')
        add_path(caves, a, b)
        add_path(caves, b, a)

    p1 = 0

    to_visit = [(a, ['start']) for a in caves['start']]

    while len(to_visit) > 0:
        (next, path) = to_visit.pop()
        if next == 'end':
            p1 += 1
            continue
        if next.islower() and next in path:
            continue

        to_visit.extend([(a, list(path) + [next])
                        for a in caves[next] if a != 'start'])

    p2 = 0

    to_visit = [(a, ['start'], False) for a in caves['start']]

    while len(to_visit) > 0:
        (next, path, small_cave_again) = to_visit.pop()
        if next == 'end':
            p2 += 1
            continue
        next_small_cave_again = small_cave_again
        if next.islower() and next in path:
            if small_cave_again:
                continue
            else:
                next_small_cave_again = True

        to_visit.extend([(a, list(path) + [next], next_small_cave_again)
                        for a in caves[next] if a != 'start'])

    return (p1, p2)


if __name__ == '__main__':
    assert solve('''start-A
start-b
A-c
A-b
b-d
A-end
b-end''') == (10, 36)

    assert solve('''fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW''') == (226, 3509)

    input = open("input/day12.txt").read().rstrip()
    (p1, p2) = solve(input)
    results(12, p1, p2)
