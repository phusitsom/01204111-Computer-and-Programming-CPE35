import numpy
def mul_matrix(A, B): return numpy.matmul(A, B).tolist()


def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f'{A[i][j]:^6}', end=' ')
        print()


print_matrix(mul_matrix(A, B))
