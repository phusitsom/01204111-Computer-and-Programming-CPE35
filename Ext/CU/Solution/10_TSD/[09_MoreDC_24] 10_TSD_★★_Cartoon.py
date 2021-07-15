cartoon = {}
x = input()
n = []
while x != 'q':
    name, atype = x.split(', ')
    if atype not in cartoon:
        cartoon[atype] = [name]
        n.append(atype)
    else:
        cartoon[atype].append(name)
    x = input()
for k in n:
    s = ''
    for j in cartoon[k]:
        s += ' ' + j + ','
    print(k + ':' + s[:-1])
