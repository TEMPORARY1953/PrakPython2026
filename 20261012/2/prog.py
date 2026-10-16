import math
from scipy.optimize import minimize_scalar
line = input()
Ws, Hs, As, Bs, form = line.split(maxsplit=4)
W = int(Ws)
H = int(Hs)
A = float(As)
B = float(Bs)
code = compile(form, "<form>", "eval")
def f(x):
	return eval(code, {"__builtins__": {}}, {"x": x, **vars(math)})
res_min = minimize_scalar(f, bounds=(A, B), method='bounded')
ymin = res_min.fun
xmin = res_min.x
res_max = minimize_scalar(lambda x: -f(x), bounds=(A, B), method='bounded')
ymax = -res_max.fun
xmax = res_max.x
delta = ymax - ymin
if delta == 0:
	delta = 1
kH = (H - 1) / delta
kW = (W - 1) / (B - A)
k = ((B - A) / (W * 30))
gr = [[' '] * W for _ in range(H)]
x = A
while x <= B:
	y = (f(x) - ymin) * kH
	gr[(H - 1) - round(y)][round(kW * (x - A))] = '*'
	x += k
for row in gr:
	print(''.join(row))
