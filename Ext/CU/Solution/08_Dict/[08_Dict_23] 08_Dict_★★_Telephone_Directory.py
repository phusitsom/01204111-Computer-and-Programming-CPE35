def reverse_d(d):
    new_d = {}
    for key in d:
        new_d[d[key]] = key
    return new_d


n = int(input())
dn = {}
for i in range(n):
    x1, x2, x3 = input().strip().split()
    dn[x1 + ' ' + x2] = x3
df = reverse_d(dn)
x = []
n = int(input())
for i in range(n):
    v = input()
    if v in dn:
        x.append(v + ' --> ' + dn[v])
    elif v in df:
        x.append(v + ' --> ' + df[v])
    else:
        x.append(v + ' --> Not found')

for i in range(len(x)):
    print(x[i])