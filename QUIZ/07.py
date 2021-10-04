N = int(input())*2-1
print(*[ f"{' '.join([ str(y) for y in x])}" for x in [[int(max(abs((N-1)/2-i),abs((N-1)/2-j))+1) for i in range(N)] for j in range(N)]],sep="\n")

# N = int(input())

# k = 2*N-1
# l, h = 0, k-1
# v = N
# mat = [[0 for __ in range(k)] for _ in range(k)]

# for i in range(N):
#     for j in range(l,h+1):
#         mat[i][j] = v
#     for j in range(l+1,h+1):
#         mat[j][i] = v
#     for j in range(l+1,h+1):
#         mat[h][j] = v
#     for j in range(l+1,h+1):
#         mat[j][h] = v

#     l+=1
#     h-=1
#     v-=1

# for x in mat:
#     for y in x:
#         print(y, end=' ')
#     print()