import sys, itertools
print(*("".join(s) for s in sorted(itertools.product("TOR", repeat=int(sys.stdin.read()))) if "".join(s).count("TOR") == 2), sep=", ")
