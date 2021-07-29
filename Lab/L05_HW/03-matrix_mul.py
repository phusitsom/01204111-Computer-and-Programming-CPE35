A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[22,13,23],[54,43,21],[23,78,71]]

import numpy
def mul_matrix(A, B): return numpy.matmul(A,B).tolist()
def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f'{A[i][j]:^6}', end = ' ')
        print()
print_matrix(mul_matrix(A,B))