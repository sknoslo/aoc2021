from lib import results


p1_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
p2_points = {")": 1, "]": 2, "}": 3, ">": 4}


def solve(input):
    lines = input.splitlines()

    p1 = 0
    p2_scores = []
    for line in lines:
        stack = []
        corrupt = False
        for c in line:
            match c:
                case "[": stack.append("]")
                case "(": stack.append(")")
                case "{": stack.append("}")
                case "<": stack.append(">")
                case _:
                    if stack.pop() != c:
                        p1 += p1_points[c]
                        corrupt = True
                        break

        if not corrupt:
            total = 0
            while len(stack) > 0:
                c = stack.pop()
                total = 5 * total + p2_points[c]
            p2_scores.append(total)

    p2_scores.sort()
    p2 = p2_scores[len(p2_scores) // 2]

    return (p1, p2)


if __name__ == '__main__':
    assert solve('''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]''') == (26397, 288957)

    input = open("input/day10.txt").read().rstrip()
    (p1, p2) = solve(input)
    results(10, p1, p2)
