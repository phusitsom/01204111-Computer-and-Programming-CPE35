d = input().split()
for i in range(len(d)):
    d[i] = int(d[i])
p = d[-1]
i = -1
j = 0
n = len(d)
while j < n-1:
    if d[j] <= p:
        i +=1
        x = d[i]
        d[i] = d[j]
        d[j] = x
    j+=1
y = d[i+1]
d[i+1] = d[-1]
d[-1] = y
print(d)