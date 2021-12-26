from lib import results


def is_int(s):
    try:
        int(s)
        return True
    except:
        return False


def execute_until(code, starting_input, vars, i):
    inputs = []

    first = True
    possible = True
    ok = True
    done = True

    for di, line in enumerate(code[i:]):
        match line.split():
            case "inp", v:
                if not first:
                    done = False
                    break
                first = False
                vars[v] = starting_input
                inputs.append(vars[v])
            case "add", v, n if is_int(n):
                vars[v] += int(n)
            case "add", v1, v2:
                vars[v1] += vars[v2]
            case "mul", v, n if is_int(n):
                vars[v] *= int(n)
            case "mul", v1, v2:
                if possible and v1 == 'z' and vars[v2] == 26:
                    ok = False
                vars[v1] *= vars[v2]
            case "div", v, n if is_int(n):
                # in the sections where z is div by 1, it is impossible to satisfy the conditional
                # and the 26x increase is inevitable
                if v == 'z' and n == '1':
                    possible = False
                vars[v] //= int(n)
            case "div", v1, v2:
                vars[v1] //= vars[v2]
            case "mod", v, n if is_int(n):
                vars[v] %= int(n)
            case "mod", v1, v2:
                vars[v1] %= vars[v2]
            case "eql", v, n if is_int(n):
                vars[v] = 1 if vars[v] == int(n) else 0
            case "eql", v1, v2:
                vars[v1] = 1 if vars[v1] == vars[v2] else 0

    return i + di, possible, ok, done


def solve(code):
    code = code.splitlines()

    p1 = 0
    p2 = 99999999999999
    stack = []
    for i in range(1, 10):
        stack.append((i, 0, {'w': 0, 'x': 0, 'y': 0, 'z': 0}, []))

    while len(stack) > 0:
        iv, line, vars, digits = stack.pop()
        digits = digits.copy()
        digits.append(iv)
        next_line, possible, ok, done = execute_until(code, iv, vars, line)
        if ok and done:
            val = 0
            for d in digits:
                val = val * 10 + d
            if val > p1:
                p1 = val
            if val < p2:
                p2 = val
            continue
        if ok or not possible:
            for i in range(1, 10):
                stack.append((i, next_line, vars.copy(), digits))

    return (p1, p2)


if __name__ == '__main__':
    code = open("input/day24.txt").read().rstrip()
    (p1, p2) = solve(code)
    results(24, p1, p2)
