N = int(input("Input the maze's size (only 1 to 9): "))
MAZE_TYPE = int(input("Input the type of maze (only 1 to 2): "))

k = 2*N-1
l, v, h = 0, 0, k-1
mat = [[0 for __ in range(k)] for _ in range(k)]

if MAZE_TYPE == 1:
    vals = sorted([i for i in range(1,N+1)],key = lambda v:v%2, reverse=1)
elif MAZE_TYPE == 2:
    vals = sorted([i for i in range(1,N+1)],key = lambda v:v%2)
    
for i in range(N):
    for j in range(l,h+1):
        mat[i][j] = vals[v]
    for j in range(l+1,h+1):
        mat[j][i] = vals[v]
    for j in range(l+1,h+1):
        mat[h][j] = vals[v]
    for j in range(l+1,h+1):
        mat[j][h] = vals[v]
    v+=1
    l+=1
    h-=1

for x in mat:
    for y in x:
        print(y, end=' ')
    print()