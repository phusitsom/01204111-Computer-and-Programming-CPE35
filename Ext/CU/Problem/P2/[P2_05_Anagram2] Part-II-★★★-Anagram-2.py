a = input()
b = input()
s1 = a.lower()
s2 = b.lower()
ans1 = {}
ans2 = {}
for i in range(len(a)):
    if 'a' <= s1[i] <= 'z':
        c = s2.find(s1[i])
        if c != -1:
            s1 = s1[:i] + '_' + s1[i+1:]
            s2 = s2[:c] + '_' + s2[c+1:]
    else:
        s1 = s1[:i] + '_' + s1[i+1:]
for i in range(len(b)):
    if 'a' <= s2[i] <= 'z':
        c = s1.find(s2[i])
        if c != -1:
            s2 = s2[:i] + '_' + s2[i+1:]
            s1 = s1[:c] + '_' + s1[c+1:]
    else:
        s2 = s2[:i] + '_' + s2[i+1:]
for i in s1:
    if 'a' <= i <= 'z':
        if i in ans1:
            ans1[i] += 1
        else:
            ans1[i] = 1
for i in s2:
    if 'a' <= i <= 'z':
        if i in ans2:
            ans2[i] += 1
        else:
            ans2[i] = 1
anss1 = []
anss2 = []
print(a)
if ans1 == {}:
    print(' - None')
else:
    for i in ans1:
        s = ' - remove ' + str(ans1[i]) + ' ' + i
        if ans1[i] > 1:
            s += "'s"
        anss1.append([i, s])
    anss1.sort()
    for i in anss1:
        print(i[1])
print(b)
if ans2 == {}:
    print(' - None')
else:
    for i in ans2:
        s = ' - remove ' + str(ans2[i]) + ' ' + i
        if ans2[i] > 1:
            s += "'s"
        anss2.append([i, s])
    anss2.sort()
    for i in anss2:
        print(i[1])
