s1 = input().strip()
data = [s1]
c = 0
try:
	while (s2 := input().strip()) != "":
		data.append(s2)
		c += 1
except EOFError:
	pass
H = len(data) - 2
W = len(data[0]) - 2
gas = 0
jewbone = 0
for i in range(1, H + 1):
	if data[i][1] == '.':
		gas += 1
	elif data[i][1] == '~':
		jewbone += 1
Hnew = W
Wnew = H
if jewbone > 0:
	jewbonenew = (jewbone * W + Wnew - 1) // Wnew
else:
	jewbonenew = 0
gasnew = Hnew - jewbonenew
if gasnew < 0:
	gasnew = 0
lresh = '#' * (Wnew + 2)
lgas = '#' + '.' * Wnew + '#'
ljewbone = '#' + '~' * Wnew + '#'
datanew = []
datanew.append(lresh)
for i in range(gasnew):
	datanew.append(lgas)
for i in range(jewbonenew):
	datanew.append(ljewbone)
datanew.append(lresh)
for i in datanew:
	print(i)
gasV = gas * W
jewboneV = jewbone * W
totalV = gasV + jewboneV
maxV = max(jewboneV, gasV)
lengas = round(20 * gasV / maxV)
lenjewbone = round(20 * jewboneV / maxV)
qgas = '.' * lengas
qjewbone = '~' * lenjewbone
fgas = str(gasV) + '/' + str(totalV)
fjewbone = str(jewboneV) + '/' + str(totalV)
maxlen = max(lengas, lenjewbone)
fw = max(len(fgas), len(fjewbone))
while len(qgas) < maxlen:
	qgas += ' '
while len(qjewbone) < maxlen:
	qjewbone += ' '
while len(fgas) < fw:
	fgas = ' ' + fgas
while len(fjewbone) < fw:
	fjewbone = ' ' + fjewbone
print(qgas + ' ' + fgas)
print(qjewbone + ' ' + fjewbone)
