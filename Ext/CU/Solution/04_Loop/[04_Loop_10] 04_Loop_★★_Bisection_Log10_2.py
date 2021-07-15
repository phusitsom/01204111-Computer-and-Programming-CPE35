a = float(input())
b = a
c = 0
while b != 0:
    c += 1
    b = b//10
L = 0
U = c
x = (L + U) / 2
while abs(a - 10 ** x) > 10 ** (-10) * max(a, 10 ** x):
    if 10 ** x > a:
        U = x
    elif 10 ** x < a:
        L = x
    x = (L + U) / 2
print(round(x, 6))
