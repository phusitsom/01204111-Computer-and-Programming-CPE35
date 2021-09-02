import numpy
A = [[1, 2], [3, 4], [5, 6]]
def transpose_matrix(A): return numpy.transpose(A).tolist()


def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f'{A[i][j]:^6}', end=' ')
        print()


print_matrix(mul_const(A, c))
