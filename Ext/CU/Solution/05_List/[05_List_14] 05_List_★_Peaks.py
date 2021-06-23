n = input().strip().split()
c = 0
for i in range(len(n)):
    n[i] = int(n[i])
for i in range(1,len(n)-1):
    if n[i] > n[i-1] and n[i] > n[i+1]:
        c += 1
print(c)