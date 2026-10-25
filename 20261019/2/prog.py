import collections

W = int(input())
texst = ""
while True:
	try:
		line = input()
	except EOFError:
		break
	if line == "":
		break
	texst += " " + line
texst = texst.lower()
newtexst = ""
for c in texst:
	if c.isalpha():
		newtexst += c
	else:
		newtexst += " "
words = newtexst.split()
newwords = []
for w in words:
	if len(w) == W:
		newwords.append(w)
if not newwords:
	exit()
count = collections.Counter(newwords)
maxc = max(count.values())
res = []
for w, c in count.items():
	if c == maxc:
		res.append(w)
res = sorted(res)
print(" ".join(res))
