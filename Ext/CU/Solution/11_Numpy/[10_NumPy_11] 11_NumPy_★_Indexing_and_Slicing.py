import numpy as np
# A is a 2-d array
def get_column_from_bottom_to_top( A, c ):
    return A[:,c][::-1]

def get_odd_rows( A ):
    return A[1::2,:]

def get_even_column_last_row( A ):
    return A[-1,::2]

def get_diagonal1( A ): # A is a square matrix # from top-left corner down to bottom-right corner
    return np.array([A[i,i] for i in range(A.shape[0])])

def get_diagonal2( A ): # A is a square matrix # from top-right corner down to bottom-left corner
    B = A[:,::-1]
    return np.array([B[i,i] for i in range(B.shape[0])])

exec(input().strip()) # ตอ้ งมคี ำสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ