def printmat(mat):
    print("sorted matrix is:")
    for i in mat:
        for j in i: print(j, end=" ")
        print()

M, N = int(input("M: ")), int(input("N: "))

mat = [[int(i) for i in input().split()] for _ in range(M)]
diag_i = [(di, r, c) for r in range(M)
          for c, di in enumerate(range(M + N - 1)[-N-r::][:N])]
diag_v = [(di, mat[r][c]) for di, r, c in diag_i]

ret_list = [[None for __ in range(N)] for _ in range(M)]
for (_, v), (_, r, c) in zip(sorted(diag_v), sorted(diag_i)):
    ret_list[r][c] = v
printmat(ret_list)
