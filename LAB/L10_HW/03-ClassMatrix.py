import numpy

class Matrix(object):
    
    def __init__(self, matrix_input) -> None:
        self.matrix = numpy.array(matrix_input)

    def __det__(self, matrix, mul=1):

        width = len(matrix)
        if width == 1:
            return mul * matrix[0][0]
        else:
            sign = -1
            answer = 0
            for i in range(width):
                m = []
                for j in range(1, width):
                    buff = []
                    for k in range(width):
                        if k != i:
                            buff.append(matrix[j][k])
                    m.append(buff)
                sign *= -1
                answer = answer + mul * self.__det__(m, sign * matrix[0][i])
        return answer

    def det(self):
        return self.__det__(self.matrix)
    
        
    def plus(self, matrix_input):
        return Matrix(numpy.add(self.matrix, matrix_input.matrix))
        
    def minus(self, matrix_input):
        return Matrix(numpy.subtract(self.matrix, matrix_input.matrix))

    def multiply(self, matrix_input):
        return Matrix(numpy.matmul(self.matrix, matrix_input.matrix))

    def show(self):
        for i, _i in enumerate(self.matrix):
            for j, _j in enumerate(_i):
                print(f'{self.matrix[i][j]:^6}', end = ' ') 
            print()

def input_matrix():
    data = []
    for i in range(3):
        data.append([int(j) for j in input(f"Row {i+1} : ").split(' ')])
    return data

print("input row of matrix A")
A = Matrix(input_matrix())
print("input row of matrix B")
B = Matrix(input_matrix())

print(f'Det of Matrix(A) = {A.det()}')
print(f'Det of Matrix(B) = {B.det()}')

print("Matrix(A+B) is:")
res = A.plus(B)
res.show()

print("Matrix(A-B) is:")
res = A.minus(B)
res.show()

print("Matrix(A*B) is:")
res = A.multiply(B)
res.show()