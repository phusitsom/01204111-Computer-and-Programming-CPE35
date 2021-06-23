def readnew(a):
	x = a.readline().split()
	if x == []:
		return ['','']
	else:
		return [x[0], x[1]]

n = input().strip().split()
f1 = open(n[0], 'r')
f2 = open(n[1], 'r')
k1 = readnew(f1)
k2 = readnew(f2)
while k1 != ['',''] and k2 != ['','']:
	if k1[0][-2:] > k2[0][-2:]:
		print(k2[0],k2[1])
		k2 = readnew(f2)
	elif k1[0][-2:] < k2[0][-2:]:
		print(k1[0],k1[1])
		k1 = readnew(f1)
	else:
		if k1[0][:2] > k2[0][:2]:
			print(k2[0],k2[1])
			k2 = readnew(f2)
		elif k1[0][:2] < k2[0][:2]:
			print(k1[0],k1[1])
			k1 = readnew(f1)
		else:
			if float(k1[1]) > float(k2[1]):
				print(k2[0],k2[1])
				k2 = readnew(f2)
			else:
				print(k1[0],k1[1])
				k1 = readnew(f1)
while k1 != ['','']:
	print(k1[0],k1[1])
	k1 = readnew(f1)
while k2 != ['','']:
	print(k2[0],k2[1])
	k2 = readnew(f2)
f1.close()
f2.close()