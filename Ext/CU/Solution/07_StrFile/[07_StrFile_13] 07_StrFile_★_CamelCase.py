s = input().strip()
ss = ''
for i in range(len(s)):
    if not s[i] in [',', '"', "'", '-', '_', '=', '.', '(', ')', '>', '<', ';', ':']:
        ss += s[i]
    else:
        ss += ' '
ss = ss.split()
for i in range(len(ss)):
    if i == 0:
        ss[0] = ss[0].lower()
    else:
        ss[i] = ss[i][0].upper() + ss[i][1:].lower()
s = ''
for i in range(len(ss)):
    s += ss[i]
print(s)