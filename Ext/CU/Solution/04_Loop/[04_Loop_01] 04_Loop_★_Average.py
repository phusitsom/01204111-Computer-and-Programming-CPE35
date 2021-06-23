n = input()
Sum = 0
c = 0
if n == 'q':
    print('No Data')
else:
    while n != 'q':
        Sum = Sum + float(n)
        n = input()
        c += 1
    print(round(Sum/c,2))