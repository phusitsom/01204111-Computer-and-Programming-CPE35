a = input()
b = input()
x = input()
c = open(a, 'r')
t = open(b, 'r')
d = open(x, 'r')
course = {}
teacher = {}
data = {}
for line in c:
    line = line.strip().split(',')
    course[line[0]] = line[1]
for line in t:
    line = line.strip().split(',')
    teacher[line[0]] = line[1]
for line in d:
    line = line.strip().split(',')
    if line[0] in course and line[1] in teacher:
        print(course[line[0]]+','+teacher[line[1]])
    else:
        print('record error')
c.close()
t.close()
d.close()
