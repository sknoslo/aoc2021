from lib import results
import sys


def print_paper(paper):
    minx, miny, maxx, maxy = sys.maxsize, sys.maxsize, 0, 0

    for (x, y) in paper:
        if x < minx:
            minx = x
        if x > maxx:
            maxx = x
        if y < miny:
            miny = y
        if y > maxy:
            maxy = y

    for y in range(miny, maxy + 1):
        line = ""
        for x in range(minx, maxx + 1):
            line += "#" if (x, y) in paper else "."
        print(line)


def do_fold(fold, paper):
    folded_paper = set(paper)
    match fold.split("="):
        case ["fold along x", sfx]:
            fx = int(sfx)
            for (x, y) in paper:
                if x > fx:
                    dx = x - fx
                    folded_paper.remove((x, y))
                    folded_paper.add((x - 2 * dx, y))
        case ["fold along y", sfy]:
            fy = int(sfy)
            for (x, y) in paper:
                if y > fy:
                    dy = y - fy
                    folded_paper.remove((x, y))
                    folded_paper.add((x, y - 2 * dy))
    return folded_paper


def solve(puzzle_input):
    lines = puzzle_input.splitlines()
    paper = set()

    i = 0
    for line in lines:
        i += 1
        if line == "":
            break
        paper.add(tuple(map(int, line.split(","))))

    instructions = lines[i:]
    first_fold = instructions[0]

    paper = do_fold(first_fold, paper)
    p1 = len(paper)

    for fold in instructions[1:]:
        paper = do_fold(fold, paper)

    print_paper(paper)

    print("")

    print("What is the code?")
    p2 = input()
    print("")

    return (p1, p2)


if __name__ == '__main__':
    assert solve('''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5''') == (17, "O")

    puzzle_input = open("input/day13.txt").read().rstrip()
    (p1, p2) = solve(puzzle_input)
    results(13, p1, p2)
