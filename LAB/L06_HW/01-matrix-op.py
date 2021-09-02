import numpy
transpose_matrix, plus_matrix, minus_matrix, mul_matrix, power_matrix = lambda m: numpy.transpose(m).tolist(), lambda a, b: numpy.add(a, b).tolist(
), lambda a, b: numpy.subtract(a, b).tolist(), lambda a, b: numpy.matmul(a, b).tolist(), lambda a, b: numpy.linalg.matrix_power(a, b).tolist()


def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f'{A[i][j]:^6}', end=' ')
        print()


print_matrix(mul_matrix(plus_matrix(A, transpose_matrix(B)),
             minus_matrix(power_matrix(C, c), D)))
