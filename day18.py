from lib import results
from itertools import permutations


class Node:
    def __init__(self, parent, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        s = "["
        s += str(self.left)
        s += ", "
        s += str(self.right)
        s += "]"
        return s

    def magnitude(self):
        l = self.left if type(self.left) == int else self.left.magnitude()
        r = self.right if type(self.right) == int else self.right.magnitude()
        return 3 * l + 2 * r


def split(number, parent):
    a = number // 2
    b = a + 1 if number / 2 > a else a
    return Node(parent, a, b)


def explode_left(node, val):
    while node.parent.left == node:
        node = node.parent
        if not node.parent:
            return
    node = node.parent
    if type(node.left) == int:
        node.left += val
        return
    node = node.left
    while type(node.right) != int:
        node = node.right
    node.right += val


def explode_right(node, val):
    while node.parent.right == node:
        node = node.parent
        if not node.parent:
            return
    node = node.parent
    if type(node.right) == int:
        node.right += val
        return
    node = node.right
    while type(node.left) != int:
        node = node.left
    node.left += val
    pass


def explode(node):
    left = node.left
    right = node.right
    explode_left(node, left)
    explode_right(node, right)
    if node == node.parent.left:
        node.parent.left = 0
    else:
        node.parent.right = 0


def reduce_explodes(node, depth=0):
    left, right = node.left, node.right

    if depth == 4:
        explode(node)
        return True

    if type(left) == Node:
        reduced = reduce_explodes(left, depth + 1)
        if reduced:
            return True

    if type(right) == Node:
        reduced = reduce_explodes(right, depth + 1)
        if reduced:
            return True

    return False


def reduce_splits(node):
    left, right = node.left, node.right

    if type(left) == Node:
        reduced = reduce_splits(left)
        if reduced:
            return True
    else:
        if left > 9:
            node.left = split(left, node)
            return True
    if type(right) == Node:
        reduced = reduce_splits(right)
        if reduced:
            return True
    else:
        if right > 9:
            node.right = split(right, node)
            return True
    return False


def add(a, b):
    node = Node(None)
    node.left = a
    node.right = b
    node.left.parent = node
    node.right.parent = node
    reduced = True
    while reduced:
        reduced = reduce_explodes(node) or reduce_splits(node)
    return node


def build_tree(number, parent=None):
    node = Node(parent)
    node.left = number[0] if type(
        number[0]) == int else build_tree(number[0], node)
    node.right = number[1] if type(
        number[1]) == int else build_tree(number[1], node)
    return node


def solve(input):
    raw = [eval(x) for x in input.splitlines()]
    numbers = [build_tree(x) for x in raw]
    count = len(numbers)

    sum = numbers[0]
    for i in range(1, len(numbers)):
        sum = add(sum, numbers[i])

    p1 = sum.magnitude()

    p2 = 0

    for ai, bi in permutations(range(count), 2):
        numbers = [build_tree(x) for x in raw]
        a = numbers[ai]
        b = numbers[bi]
        c = add(a, b)
        m = c.magnitude()
        if m > p2:
            p2 = m

    return (p1, p2)


if __name__ == '__main__':
    assert solve('''[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]''') == (4140, 3993)

    input = open("input/day18.txt").read().rstrip()
    (p1, p2) = solve(input)
    results(18, p1, p2)
