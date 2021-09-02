A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[22, 13, 23], [54, 43, 21], [23, 78, 71]]


def minus_matrix(A, B):
    return list(map(lambda i: list(map(lambda x, y: x - y, A[i], B[i])), range(len(A))))


def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f'{A[i][j]:^6}', end=' ')
        print()


print_matrix(minus_matrix(A, B))
