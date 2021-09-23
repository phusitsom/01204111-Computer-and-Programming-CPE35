from itertools import permutations
inp = [input().split() for _ in range(int(input("N : ")))]
cal = int(input('XX : '))
for perm in permutations(inp):
    s, names = 0, []
    for n, e in perm:
        s, names = s+int(e), names+[n]
        if s >= cal: break
    if s == cal: break
print(*names)