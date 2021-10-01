import numpy as np
from copy import deepcopy

L, W = int(input('Length: ')), input('Width: ')
MAP = [[int(j) for j in input().split()] for i in range(L)]
NEW_MAP = np.array([sl[1:-1] for sl in  MAP[1:-1]])

print_list = []
for x, y in np.argwhere(NEW_MAP):
    indexes = [(x+i, y+j) for j in range(2) for i in range(4)]
    try:
        if all([NEW_MAP[i][j] for i,j in indexes]):
            p_map = deepcopy(MAP)
            for i, j in indexes: p_map[i+1][j+1] = 'x'
            print_list.append(p_map)
    except IndexError: pass

print(f"{len(print_list)} possible court(s)")
for l in print_list:
    for x in l:
        for y in x: print(y, end=" ")
        print()
    print()