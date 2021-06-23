import numpy as np

inp = int(input())
def stirlingsapprox(n):
    lower = np.sqrt(2*np.pi) * (n**(n+(1/2))) * (np.exp(1) **  (-n + (1/((12*n)+1))))
    upper = np.sqrt(2*np.pi) * (n**(n+(1/2))) * (np.exp(1) **  (-n + (1/(12*n))))
    
    return lower, upper

result = stirlingsapprox(inp)
print('{}\n{}'.format(result[0],result[1]))