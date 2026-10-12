from decimal import Decimal, getcontext
def esum(N, one):
    total = one
    term = one
    for n in range(1, N + 1):
        term = term / n
        total += term
    return total
print("float:  ", esum(20, 1.0))
for prec in (10, 20, 30, 50):
    getcontext().prec = prec
    print(f"prec={prec:>2}:", esum(50, Decimal(1)))
