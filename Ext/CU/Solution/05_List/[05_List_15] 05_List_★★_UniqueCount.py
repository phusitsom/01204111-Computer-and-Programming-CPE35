n = input().strip().split()
c = 0
for i in range(len(n)):
    n[i] = int(n[i])
n.sort()
ans = []
for i in range(len(n)):
    if n[i] == n[i-1]:
        c += 0
    else:
        if c < 10:
            ans.append(n[i])
        c += 1
print(c)
print(ans)
