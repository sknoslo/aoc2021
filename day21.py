from lib import results

possible_rolls = []
for a in range(1, 4):
    for b in range(1, 4):
        for c in range(1, 4):
            possible_rolls.append(a + b + c)


def do_p2(players, scores=[0, 0], turn=0, cache=dict()):
    p = turn % 2

    key = (players[0], players[1], scores[0], scores[1], p)

    if max(scores) >= 21:
        return [1 if scores[0] >= 21 else 0, 1 if scores[1] >= 21 else 0]

    if key in cache:
        return cache[key]

    ways_to_win = [0, 0]
    for roll in possible_rolls:
        next_players = list(players)
        next_scores = list(scores)

        next_players[p] = (next_players[p] + roll) % 10
        if next_players[p] == 0:
            next_players[p] = 10
        next_scores[p] += next_players[p]
        p1_wins, p2_wins = do_p2(next_players, next_scores, turn + 1, cache)
        ways_to_win[0] += p1_wins
        ways_to_win[1] += p2_wins
    cache[key] = ways_to_win
    return ways_to_win


def solve(input):
    lines = input.splitlines()

    players = [int(lines[0].split()[-1]), int(lines[1].split()[-1])]

    scores = [0, 0]

    next_roll = 1
    rolls = 0

    while max(scores) < 1000:
        player = rolls % 2
        dist = 0
        for _ in range(3):
            dist += next_roll
            next_roll = (next_roll + 1) % 100
            if next_roll == 0:
                next_roll = 100

            rolls += 1
        players[player] = (players[player] + dist) % 10
        if players[player] == 0:
            players[player] = 10
        scores[player] += players[player]

    p1 = min(scores) * rolls

    p2 = max(do_p2([int(lines[0].split()[-1]),
                    int(lines[1].split()[-1])]))

    return (p1, p2)


if __name__ == '__main__':
    assert solve('''Player 1 starting position: 4
Player 2 starting position: 8''') == (739785, 444356092776315)

    input = open("input/day21.txt").read().rstrip()
    (p1, p2) = solve(input)
    results(21, p1, p2)
