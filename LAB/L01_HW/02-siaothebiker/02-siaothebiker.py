a = int(input('A : '))
b = int(input('B : '))
x = int(input('X : '))

dS_a = x/a
dS_b = x/b
print('Wait :', int((dS_a - dS_b)*(60**2)), 'sec')
