height = float(input('Hight : '))
price = float(input('Cost : '))

def is_corruption(h, p):
    if (h < 1) & (p < 1000): 
        print('NO')
    elif (h > 1) & (h < 4) & (p < 5000): 
        print('NO')
    elif (h > 4) & (h < 8) & (p < 30000): 
        print('NO')
    elif (h > 8) & (p < 75000): 
        print('NO')
    else: print('YES')

is_corruption(height, price)