s = input()
n = ['0','1','2','3','4','5','6','7','8','9']
x = ''
for i in range(len(s)):
    for j in range(10):
        if s[i] == n[j]:
            n[j] = ''
if n == ['','','','','','','','','','']:
    print('None')
else:
    for i in range(10):
        if n[i] != '':
            x = x + n[i] + ','
    print(x[0:-1])