import numpy as np
n, m = [int(input(f"Input {t}: ")) for t in ['n', 'm']]
arr = np.array([[int(i) for i in input().split()] for _ in range(n)])
for v in np.sort(arr.flatten()): 
    print('({},{})'.format(*np.argwhere(arr==v)[0]))