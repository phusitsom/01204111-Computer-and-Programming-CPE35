import math
bd, bm, by, d, m, y = [int(e) for e in input().split()]
nb_day = 0
n_day = 0
nb_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
n_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
by -= 543
y -= 543
if by % 400 == 0 or (by % 100 != 0 and by % 4 == 0):
    nb_month[2] = 29
if y % 400 == 0 or (y % 100 != 0 and y % 4 == 0):
    n_month[2] = 29
for i in range(1, 13):
    if i > bm:
        nb_day += nb_month[i]
    if i < m:
        n_day += n_month[i]
nb_day += nb_month[bm]-bd+1
n_day += d-1
n_year = (y-by-1)*365
t = nb_day + n_day + n_year
x = math.sin(2*math.pi*t/23)
y = math.sin(2*math.pi*t/28)
z = math.sin(2*math.pi*t/33)
print(t, "{:.2f}".format(x), "{:.2f}".format(y), "{:.2f}".format(z))