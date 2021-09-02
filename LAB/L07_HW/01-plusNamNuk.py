N = int(input("N : "))
for v in ["=".join(input().split()) for _ in range(N)]:
    exec(v)
print(eval(input()))
