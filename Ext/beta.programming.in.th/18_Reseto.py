N, K = map(int, input().split())
number = []
cut = []
for i in range(2, N+1, 1):
    number.append(i)
while len(number) != 0:
    P = min(number)
    for i in number:
        if i % P == 0:
            number.remove(i)
            cut.append(i)
print(cut[K-1])
