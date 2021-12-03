from lib import results


def get_gamma_epsilon(numbers, digits):
    gamma = 0
    epsilon = 0
    for digit in range(digits):
        c = 0
        for number in numbers:
            c += number >> digit & 1

        if c >= len(numbers) / 2:
            gamma |= 1 << digit
        else:
            epsilon |= 1 << digit

    return (gamma, epsilon)


def solve(input):
    lines = input.splitlines()
    digits = len(lines[0])
    numbers = [int(x, 2) for x in lines]

    (gamma, epsilon) = get_gamma_epsilon(numbers, digits)
    p1 = epsilon * gamma

    o_numbers = numbers
    co_numbers = numbers

    for digit in range(digits):
        (o_gamma, _) = get_gamma_epsilon(o_numbers, digits)
        (_, co_epsilon) = get_gamma_epsilon(co_numbers, digits)
        mask = 1 << (digits - digit - 1)
        if len(o_numbers) > 1:
            o_numbers = [x for x in o_numbers if x & mask == o_gamma & mask]
        if len(co_numbers) > 1:
            co_numbers = [x for x in co_numbers if x &
                          mask == co_epsilon & mask]
    p2 = o_numbers[0] * co_numbers[0]

    return (p1, p2)


if __name__ == '__main__':
    assert solve('''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010''') == (198, 230)

    input = open("input/day03.txt").read().rstrip()
    (p1, p2) = solve(input)
    results(3, p1, p2)
