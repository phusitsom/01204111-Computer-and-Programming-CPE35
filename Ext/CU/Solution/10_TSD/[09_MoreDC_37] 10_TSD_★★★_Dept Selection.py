n = int(input())
num = {}
code = []
ans = {}
for i in range(n):
    s = input().strip().split()
    num[s[0]] = int(s[1])
n = int(input())
for i in range(n):
    c = input().strip().split()
    code.append([float(c[1]), c[0], c[2:]])
code = sorted(code, reverse=True)
for score, code, area in code:
    for choose in area:
        if num[choose] > 0:
            ans[code] = choose
            num[choose] -= 1
            break
for i in sorted(ans):
    print(i, ans[i])
