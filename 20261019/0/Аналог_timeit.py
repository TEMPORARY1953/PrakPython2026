from timeit import Timer
s = "pass"
stmt = input("Сниппет: ")
t = Timer(stmt=stmt, s=s)
n, time_taken = t.autorange()
print(f"n = {n}")
print(f"total  = {time_taken:.6f} s")
print(f"per loop = {time_taken / n * 1e6:.3f} µs")
