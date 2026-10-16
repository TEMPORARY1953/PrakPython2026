import fractions

strr = input().strip()
sp = [p.strip() for p in strr.split(',')]
i = 0
s = fractions.Fraction(sp[i])
i += 1
w = fractions.Fraction(sp[i])
i += 1
dA = int(sp[i])
i += 1
keffA = []
for j in range(dA + 1):
	keffA.append(fractions.Fraction(sp[i]))
	i += 1
dB = int(sp[i])
i += 1
keffB = []
for j in range(dB + 1):
	keffB.append(fractions.Fraction(sp[i]))
	i += 1
A = fractions.Fraction(0)
for j in range(dA, -1, -1):
	A += keffA[j] * (s**(dA - j))
B = fractions.Fraction(0)
for j in range(dB, -1, -1):
	B += keffB[j] * (s**(dB - j))
if B != fractions.Fraction(0):
	q = A / B
	if q == w:
		print("True")
	else:
		print("False")
else:
	print("False")
