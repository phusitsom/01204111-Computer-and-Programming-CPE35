n = int(input())
A = set({})
B = set({})
for i in range(n):
    s = set(input().split())
    if i == 0:
        A = s
        B = s
    else:
        A = A | s
        B = B & s
print(len(A))
print(len(B))