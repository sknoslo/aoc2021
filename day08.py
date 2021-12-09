from lib import results
from more_itertools import flatten


def decode_input(input):
    zero = one = two = three = four = five = six = seven = eight = nine = None
    zsn = []
    ttf = []

    for i in input:
        match len(i):
            case 2: one = i
            case 4: four = i
            case 3: seven = i
            case 7: eight = i
            case 5: ttf.append(i)
            case 6: zsn.append(i)

    s_one = set(one)
    s_four = set(four)

    for i in zsn:
        s_i = set(i)
        if s_i & s_four == s_four:
            nine = i
        elif len(s_one - s_i) == 0:
            zero = i
        else:
            six = i

    f = s_one - set(six)

    for i in ttf:
        s_i = set(i)
        if s_i & s_one == s_one:
            three = i
        elif s_i & f == f:
            two = i
        else:
            five = i

    return {zero: '0', one: '1', two: '2', three: '3', four: '4', five: '5', six: '6', seven: '7', eight: '8', nine: '9'}


def solve(input):
    lines = input.splitlines()
    data = [(i.split(), o.split())
            for (i, o) in [tuple(x.split(' | ')) for x in lines]]

    unique = list(filter(lambda x: len(x) != 5 and len(
        x) != 6, flatten([x[1] for x in data])))

    p1 = len(unique)

    p2 = 0
    for (input_line, output_line) in data:
        input_line = ["".join(sorted(x)) for x in input_line]
        output_line = ["".join(sorted(x)) for x in output_line]

        number_map = decode_input(input_line)

        output_number = ""
        for digit in output_line:
            output_number += number_map[digit]

        p2 += int(output_number)

    return (p1, p2)


if __name__ == '__main__':
    assert solve('''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce''') == (26, 61229)

    input = open("input/day08.txt").read().rstrip()
    (p1, p2) = solve(input)
    results(8, p1, p2)
