g = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A']
ids = []
grade = []
s = input()
while s != 'q':
    s = s.split()
    ids.append(s[0])
    grade.append(s[1])
    s = input()
up_id = input().split()
for i in range(len(up_id)):
    x = ids.index(up_id[i])
    y = g.index(grade[x])
    if y != 7:
        grade[x] = g[y+1]
a = []
for i in range(len(ids)):
    m = [int(ids[i]), grade[i]]
    a.append(m)
a.sort()
for i in range(len(ids)):
    print(a[i][0], a[i][1])
