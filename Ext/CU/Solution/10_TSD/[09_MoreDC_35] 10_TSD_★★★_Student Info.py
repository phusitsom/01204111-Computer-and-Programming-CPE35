n = int(input())
name = []
data = {}
ans = {}
for i in range(n):
    s = input().strip()
    ss = s.split()
    data[ss[0]] = ss[1:]
    name.append(ss[0])
x = input().strip().split()
for i in x:
    c = 0
    while c < len(name):
        if i not in data[name[c]]:
            name.remove(name[c])
            c -= 1
        c += 1
if name == []:
    print('Not Found')
else:
    for i in sorted(name):
        print(i, data[i][0], data[i][1], data[i][2])
