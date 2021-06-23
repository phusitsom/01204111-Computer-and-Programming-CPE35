s = input().strip()
s = s.lower()
d = {}
for i in range(len(s)):
	if s[i] in 'abcdefghijklmnopqrstuvwxyz':
		if s[i] in d:
			d[s[i]] += 1
		else:
			d[s[i]] = 1
x = []
for key in d:
	x.append([-int(d[key]),key])
x.sort()
for i in range(len(d)):
	print(x[i][1],'->',-int(x[i][0]))