import itertools

def slide(seq, n):
	it = iter(seq)
	itn = itertools.tee(it, len(seq))
	for i in range(len(seq)):
		yield from itertools.islice(itn[i], i, n + i)

import sys
exec(sys.stdin.read())
