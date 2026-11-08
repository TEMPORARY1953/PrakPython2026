import sys, itertools
print(*filter(lambda s: s.count("TOR") == 2, ("".join(s) for s in sorted(itertools.product("TOR", repeat=int(sys.stdin.read()))))), sep=", ")
