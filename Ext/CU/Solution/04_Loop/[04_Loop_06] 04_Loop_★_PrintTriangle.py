n = int(input())
for i in range(n):
    if i == 0:
        print(str(' ' * (n - 1)) + '*')
    elif i == (n-1):
        print('*' * (2 * n - 1))
    else:
        print(str(' ' * (n - 1 - i)) + '*', end='')
        print(str(' ' * (2 * i - 1)) + '*' )