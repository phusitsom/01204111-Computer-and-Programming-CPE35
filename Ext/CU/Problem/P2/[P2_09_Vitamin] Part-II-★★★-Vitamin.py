n = int(input())  # อ่ำนจ ำนวนผลไม้
vit = []
for i in range(n):
    v = input().strip().split()
    vit.append(v)

c = input().split()  # อ่ำนค ำสั่งที่ต้องกำรประมวลผล
if c[0] == 'show':
    show = ''
    for i in vit:
        for j in i:
            show += j + ' '
        print(show)
        show = ''

elif c[0] == 'max':
    max_ = []
    for i in vit:
        max_.append([-float(i[int(c[1])]), i[0]])
    max_.sort()
    print(max_[0][1], -(max_[0][0]))

elif c[0] == 'avg':
    avg = 0
    for i in vit:
        avg += float(i[int(c[1])])
    print(round(avg / n, 4))

elif c[0] == 'get':
    ch = False
    for i in vit:
        if c[1] == i[0]:
            for j in i:
                print(j, end=' ')
            ch = True
    if not ch:
        print(c[1], 'not found')

elif c[0] == 'sort':
    sort_ = []
    for i in vit:
        sort_.append([float(i[int(c[1])]), i[0]])
    sort_.sort()
    for i in sort_:
        print(i[1], end=' ')
