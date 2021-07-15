d1 = input().replace(',', '').split()
d2 = input().replace(',', '').split()
month = ['January', 'February', 'March', 'April', 'May', 'June',
         'July', 'August', 'September', 'October', 'November', 'December']
m = [0, 0]
for i in range(12):
    if d1[1] == month[i]:
        m[0] = i
    if d2[1] == month[i]:
        m[1] = i
if d1[1:] == d2[1:]:
    print(d1[0], d2[0])
else:
    if int(d1[3]) < int(d2[3]):
        check = d1[0]
    elif int(d1[3]) > int(d2[3]):
        check = d2[0]
    elif m[0] < m[1]:
        check = d1[0]
    elif m[0] > m[1]:
        check = d2[0]
    elif int(d1[2]) < int(d2[2]):
        check = d1[0]
    else:
        check = d2[0]
    print(check)
