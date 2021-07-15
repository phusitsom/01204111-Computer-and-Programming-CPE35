def pattern1(nrows, ncols):
    x = []
    c = 1
    for i in range(1, nrows+1):
        y = []
        for j in range(i, i+ncols):
            y.append(c)
            c += 1
        x.append(y)
    return x


def pattern2(nrows, ncols):
    x = []
    for i in range(1, nrows+1):
        y = []
        for j in range(i, nrows*ncols-nrows+i+1, nrows):
            y.append(j)
        x.append(y)
    return x


def pattern3(N):
    c = 1
    x = []
    for i in range(N):
        y = [0 for i in range(i)]
        for k in range(N-i):
            y.append(c)
            c += 1
        x.append(y)
    return x


def pattern4(N):
    c = 1
    x = []
    for i in range(N):
        y = [0 for i in range(i)]
        x.append(y)
    for i in range(N):
        for j in range(i, -1, -1):
            x[j].append(c)
            c += 1
    return x


def pattern5(N):
    c = 1
    x = []
    for i in range(N):
        y = [0 for i in range(i)]
        x.append(y)
    for i in range(N):
        for j in range(N-i):
            x[j].append(c)
            c += 1
    return x


def pattern6(N):
    c = 1
    x = []
    for i in range(N):
        y = [0 for i in range(i)]
        x.append(y)
    for i in range(N):
        if i % 2 == 0:
            for j in range(N - i):
                x[j].append(c)
                c += 1
        else:
            for j in range(N-i-1, -1, -1):
                x[j].append(c)
                c += 1
    return x


exec(input().strip())
