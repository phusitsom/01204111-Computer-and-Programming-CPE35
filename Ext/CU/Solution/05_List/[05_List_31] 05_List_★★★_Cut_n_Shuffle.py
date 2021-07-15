s = input().split()
c = input()
for i in range(len(c)):
    if c[i] == 'C':
        a = s[:len(s)//2]
        b = s[len(s)//2:]
        b.extend(a)
        s = b
    if c[i] == 'S':
        x = []
        for j in range(len(s)//2):
            x.append(s[j])
            x.append(s[len(s)//2+j])
        s = x
for i in range(len(s)):
    print(s[i], end=" ")
