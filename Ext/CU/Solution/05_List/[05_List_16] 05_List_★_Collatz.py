n = int(input())
L = [n]
s = ''
while n != 1:
    if n % 2 == 0:
        n = n // 2
        L.append(n)
    else:
        n = 3*n + 1
        L.append(n)
if len(L)<=15:
    for i in range(len(L)-1):
        s = s[0:] + str(L[i]) + '->'
    s = s[0:] + str(L[-1])
else:
    for i in range(14):
        s = s[0:] + str(L[-15+i]) + '->'
    s = s[0:] + str(L[-1])
print(s)