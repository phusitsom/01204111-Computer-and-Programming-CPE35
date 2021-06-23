import math

def mosteller(W,H):
    result = math.sqrt(W*H)/60
    return result

def haycock(W,H):
    result = 0.024265 * (W ** 0.5378) * (H ** 0.3964)
    return result

def boyd(W,H):
    result = 0.0333 * (W ** (0.6157 - 0.0188 * math.log10(W))) * (H ** 0.3)
    return result

def all_eq(W,H):
    print('{}\n{}\n{}'.format(mosteller(W,H),haycock(W,H),boyd(W,H)))
    
w = float(input())
h = float(input())
all_eq(w,h)