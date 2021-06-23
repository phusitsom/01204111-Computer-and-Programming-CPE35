import numpy as np
a = float(input())
b = float(input())
c = float(input())

def sqal(a,b,c):
    x1 = (-b-np.sqrt((b**2)-4*a*c))/(2*a)
    x2 = (-b+np.sqrt((b**2)-4*a*c))/(2*a)
    
    return x1, x2

result = sqal(a,b,c)
print('{:.3f} {:.3f}'.format(result[0], result[1]))