# from datetime import date
d, m, y = int(input('d: ')), int(input('m: ')), int(input('y: '))
# date_val = date(y, m, d)
# print(int(date_val.strftime('%j')))
if (y%400 == 0 ) or (y%4 == 0) and (y%100 != 0): leap = True
else: leap = False
