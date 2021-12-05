from lib import results
from more_itertools import chunked


def mark_number(board, number):
    for i in range(len(board)):
        match board[i]:
            case (x, _) if x == number: board[i] = (x, True)


def is_marked(board, x, y):
    match board[x + y * 5]:
        case (_, marked): return marked


def check_board(board):
    for a in range(5):
        h_good = True
        v_good = True
        for b in range(5):
            h_good &= is_marked(board, a, b)
            v_good &= is_marked(board, b, a)
        if h_good or v_good:
            return True
    return False


def mark_and_check(boards, number):
    winners = []
    for board in boards:
        mark_number(board, number)

    for board in boards:
        if check_board(board):
            winners.append(board)
    return winners


def score(board, number):
    sum = 0
    for (x, marked) in board:
        if not marked:
            sum += x
    return sum * number


def parse_input(input):
    input = input.split()

    draw_numbers = [int(x) for x in input[0].split(",")]
    boards = list(chunked([(int(x), False) for x in input[1:]], 25))

    return (draw_numbers, boards)


def solve(input):
    (draw_numbers, boards) = parse_input(input)

    p1 = None
    p2 = None
    for number in draw_numbers:
        winners = mark_and_check(boards, number)
        if len(winners) > 0:
            if not p1:
                p1 = score(winners[0], number)

            for winner in winners:
                boards.remove(winner)

                if len(boards) == 0:
                    p2 = score(winner, number)

    return (p1, p2)


if __name__ == '__main__':
    assert solve('''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7''') == (4512, 1924)

    input = open("input/day04.txt").read().rstrip()
    (p1, p2) = solve(input)
    results(4, p1, p2)
