n = int(input())
c = 0
ans = []
for i in range(n):
    x = int(input())
    if c % 2 == 0:
        ans.append(x)
        c += 1
    else:
        ans.insert(0, x)
        c += 1
x = input().strip().split()
for i in range(len(x)):
    if c % 2 == 0:
        ans.append(int(x[i]))
        c += 1
    else:
        ans.insert(0, int(x[i]))
        c += 1
x = int(input())
while(x != -1):
    if c % 2 == 0:
        ans.append(x)
        c += 1
    else:
        ans.insert(0, x)
        c += 1
    x = int(input())
print(ans)
