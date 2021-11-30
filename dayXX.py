from lib import results

def solve(input):
	return (None, None)

if __name__ == '__main__':
	assert solve("abc") == (None, None)

	input = open("input/dayXX.txt").read().rstrip()
	(p1, p2) = solve(input)
	results(0, p1, p2)
