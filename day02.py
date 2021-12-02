from lib import results


def simple(instructions):
    depth = 0
    hpos = 0

    for instruction in instructions:
        match instruction:
            case ("forward", x): hpos += x
            case ("up", x): depth -= x
            case ("down", x): depth += x

    return depth * hpos


def complex(instructions):
    aim = 0
    depth = 0
    hpos = 0

    for instruction in instructions:
        match instruction:
            case ("forward", x):
                hpos += x
                depth += aim * x
            case ("up", x): aim -= x
            case ("down", x): aim += x

    return depth * hpos


def solve(input):
    instructions = [(instruction[0], int(instruction[1])) for instruction in [
        line.split() for line in input.splitlines(False)]]

    return (simple(instructions), complex(instructions))


if __name__ == '__main__':
    assert solve('''forward 5
down 5
forward 8
up 3
down 8
forward 2''') == (150, 900)

    input = open("input/day02.txt").read().rstrip()
    (p1, p2) = solve(input)
    results(2, p1, p2)
