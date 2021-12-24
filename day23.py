from lib import results
from heapq import heappush, heappop


costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
entries = {'A': 3, 'B': 5, 'C': 7, 'D': 9}

waiting_spaces = [('H', 1), ('H', 2), ('H', 4), ('H', 6),
                  ('H', 8), ('H', 10), ('H', 11)]


paths = dict()


def get_path(curr, dest):
    if (curr, dest) in paths:
        return paths[(curr, dest)]
    path = set()
    if curr[0] == 'H':
        entry_pos = entries[dest[0]]
        s = min(curr[1], entry_pos)
        e = max(curr[1], entry_pos)
        for i in range(s, e + 1):
            if i == curr[1]:
                continue
            path.add(('H', i))
        for i in range(1, dest[1] + 1):
            path.add((dest[0], i))
    elif dest[0] == 'H':
        for i in range(1, curr[1]):
            path.add((curr[0], i))
        entry_pos = entries[curr[0]]
        s = min(dest[1], entry_pos)
        e = max(dest[1], entry_pos)
        for i in range(s, e + 1):
            path.add(('H', i))
    else:
        s = min(entries[curr[0]], entries[dest[0]])
        e = max(entries[curr[0]], entries[dest[0]])
        for i in range(s, e + 1):
            path.add(('H', i))
        for i in range(1, dest[1] + 1):
            path.add((dest[0], i))
        for i in range(1, curr[1]):
            path.add((curr[0], i))

    paths[(curr, dest)] = path
    return path


def path_is_clear(state, curr, dest):
    path = get_path(curr, dest)
    for p in path:
        for a in state:
            if (a[1] == p):
                return False
    return True


def find_open_room_spot(state, a, default):
    taken = []
    for o, (id, spot), _ in state:
        if id == a and o != a:
            return None
        if id == a:
            taken.append(spot)
    if len(taken) == 0:
        return default
    return min(taken) - 1


def cost_of_path(a, curr, dest):
    path = get_path(curr, dest)
    return costs[a[0]] * len(path)


def do_it(initial_state, room_size):
    q = []

    seen = set()

    heappush(q, initial_state)

    while len(q) > 0:
        state = heappop(q)

        if state in seen:
            continue

        seen.add(state)

        cost = state[0]

        done = True
        for a in state[1:]:
            if a[0] != a[1][0]:
                done = False
                break
        if done:
            return cost

        for i, a in enumerate(state[1:]):
            if a[2] == 2 or (a[0] == a[1][0] and a[1][1] == 2):
                # can't move any more
                continue

            # try for final destination if not already in correct room and rooms is suitable
            if a[0] != a[1][0]:
                open_room_spot = find_open_room_spot(
                    state[1:], a[0], room_size)
                if open_room_spot != None:
                    destination = (a[0], open_room_spot)
                    if path_is_clear(state[1:], a[1], destination):
                        next_state = list(state)
                        next_state[0] = cost + \
                            cost_of_path(a[0], a[1], destination)
                        next_state[i + 1] = (a[0], destination, 2)
                        heappush(q, tuple(next_state))
            if a[2] == 0:
                # can go to waiting spaces if never moved before
                for s in waiting_spaces:
                    if path_is_clear(state[1:], a[1], s):
                        next_state = list(state)
                        next_state[0] = cost + cost_of_path(a[0], a[1], s)
                        next_state[i + 1] = (a[0], s, 1)
                        heappush(q, tuple(next_state))


def solve(input):
    amphipods = [c for c in input if c in {'A', 'B', 'C', 'D'}]

    initial_state = (
        0,
        (amphipods[0], ('A', 1), 0),
        (amphipods[1], ('B', 1), 0),
        (amphipods[2], ('C', 1), 0),
        (amphipods[3], ('D', 1), 0),
        (amphipods[4], ('A', 2), 0),
        (amphipods[5], ('B', 2), 0),
        (amphipods[6], ('C', 2), 0),
        (amphipods[7], ('D', 2), 0)
    )

    p1 = do_it(initial_state, 2)

    initial_state = (
        0,
        (amphipods[0], ('A', 1), 0),
        (amphipods[1], ('B', 1), 0),
        (amphipods[2], ('C', 1), 0),
        (amphipods[3], ('D', 1), 0),
        ('D', ('A', 2), 0),
        ('C', ('B', 2), 0),
        ('B', ('C', 2), 0),
        ('A', ('D', 2), 0),
        ('D', ('A', 3), 0),
        ('B', ('B', 3), 0),
        ('A', ('C', 3), 0),
        ('C', ('D', 3), 0),
        (amphipods[4], ('A', 4), 0),
        (amphipods[5], ('B', 4), 0),
        (amphipods[6], ('C', 4), 0),
        (amphipods[7], ('D', 4), 0)
    )

    p2 = do_it(initial_state, 4)

    return (p1, p2)


if __name__ == '__main__':
    assert solve('''#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########''') == (12521, 44169)

    input = open("input/day23.txt").read().rstrip()
    (p1, p2) = solve(input)
    results(23, p1, p2)
