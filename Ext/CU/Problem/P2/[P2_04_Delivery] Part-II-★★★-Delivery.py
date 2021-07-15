pk = input()
ans = []
anss = []
month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
         7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
date_deli = {'E': 1, 'Q': 3, 'N': 7, 'F': 14}
while pk != 'END':
    pkk = pk.strip().split()
    num, deli, d, m, y = pkk[0], pkk[1], int(pkk[2]), int(pkk[3]), int(pkk[4])
    error = False
    if (y-543) % 400 == 0 or ((y-543) % 100 != 0 and (y-543) % 4 == 0):
        month[2] = 29
    else:
        month[2] = 28
    if y < 2558:
        ans.append('Error: ' + pk + ' --> Invalid year')
        error = True
    elif m < 1 or m > 12:
        ans.append('Error: ' + pk + ' --> Invalid month')
        error = True
    elif not 0 < d <= month[m]:
        ans.append('Error: ' + pk + ' --> Invalid date')
        error = True
    elif not deli in ['E', 'Q', 'N', 'F']:
        ans.append('Error: ' + pk + ' --> Invalid delivery type')
        error = True
    if not error:
        d += date_deli[deli]
        if d > month[m]:
            d -= month[m]
            m += 1
        if m > 12:
            m -= 12
            y += 1
        s = str(num) + ': delivered on '+str(d)+'/'+str(m)+'/'+str(y)
        anss.append([y, m, d, num, s])
    pk = input()
anss.sort()
for i in ans:
    print(i)
for i in anss:
    print(i[4])
