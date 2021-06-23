def reverse_d(d):
    new_d = {}
    for key in d:
        new_d[d[key]] = key
    return new_d


n = int(input())
dn = {}
for i in range(n):
    x1, x2 = input().strip().split()
    dn[x1] = x2
df = reverse_d(dn)
x = []
n = int(input())
for i in range(n):
    v = input()
    if v in dn:
        x.append(dn[v])
    elif v in df:
        x.append(df[v])
    else:
        x.append('Not found')

for i in range(len(x)):
    print(x[i])