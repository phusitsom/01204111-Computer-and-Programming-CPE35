U1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
L1 = 'abcdefghijklmnopqrstuvwxyz'
ans = []
s = input()
while s != 'end':
    m = ''
    for i in range(len(s)):
        if s[i] in U1:
            m += U1[( U1.find(s[i]) + 13) %26]
        elif s[i] in L1:
            m += L1[( L1.find(s[i]) + 13) %26]
        else:
            m += s[i]
    ans.append(m)
    s = input()
for i in range(len(ans)):
    print(ans[i])