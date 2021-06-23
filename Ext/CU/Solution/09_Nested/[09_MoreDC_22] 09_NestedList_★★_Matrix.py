def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append( float(e) )
        m.append(r)
    return m

def mult_c(c, A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] *= c
    return A

def mult(A, B):
    X = []
    for i in range(len(A)):
        C = []
        for j in range(len(B[0])):
            m = 0
            for k in range(len(B)):
                m += A[i][k] * B[k][j]
            C.append(m)
        X.append(C)
    return X

exec(input().strip()) # ตอ้ งมคี ำสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ