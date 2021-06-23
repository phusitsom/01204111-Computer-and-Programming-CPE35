s1 = input().strip()
s2 = input().strip()
ss1 = ''
ss2 = ''
for i in range(len(s1)):
    if not s1[i] == ' ':
        ss1 += s1[i]
for i in range(len(s2)):
    if not s2[i] == ' ':
        ss2 += s2[i]
ss1 = ss1.lower()
ss2 = ss2.lower()
if len(ss1) != len(ss2):
    print('NO')
else:
    for i in range(len(ss1)):
        if ss1[i] in ss2:
            x = ss2.find(ss1[i])
            ss2 = ss2[0:x] + ss2[x+1:]
    if len(ss2) == 0:
        print('YES')
    else:
        print('NO')