n = int(input())
icecream = {}
for i in range(n):
    x, y = input().strip().split()
    icecream[x] = int(y)
c = []
m = int(input())
sale_ice = {}
for i in range(m):
    x, y = input().strip().split()
    if x in icecream:
        if x in sale_ice:
            sale_ice[x] += icecream[x] * int(y)
        else:
            sale_ice[x] = icecream[x] * int(y)
if sale_ice == {}:
    print('No ice cream sales')
else:
    c = 0
    for k in sale_ice:
        c += sale_ice[k]
    print('Total ice cream sales:', float(c))
    x = []
    for k in sale_ice:
        x.append([sale_ice[k], k])
    x.sort()
    top = ''
    m = x[len(x)-1][0]
    for i in range(len(x)):
        if m == x[i][0]:
            if top == '':
                top = x[i][1]
            else:
                top += ', '+x[i][1]
    print('Top sales:', top)
