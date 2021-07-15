def row_number(t, e):  # return row number of t containing e (top row is row #0)
    for i in range(len(t)):
        if e in t[i]:
            return i


def flatten(t):  # return a list of ints converted from list of lists of ints t
    x = []
    for i in range(len(t)):
        for j in range(len(t[i])):
            if t[i][j] != 0:
                x.append(t[i][j])
    return x


def inversions(x):  # return the number of inversions of list x
    c = 0
    for i in range(len(x)-1):
        for j in x[i+1:]:
            if x[i] > j:
                c += 1
    return c


def solvable(t):  # return True if tiling t (list of lists of ints) is solvable
    x = flatten(t)
    c = inversions(x)
    if len(x) % 2 == 0 and c % 2 == 0:
        return True
    else:
        p0 = row_number(t, 0)
        if c % 2 != 0 and p0 % 2 == 0:
            return True
        if c % 2 == 0 and p0 % 2 != 0:
            return True
    return False


exec(input().strip())
