n = int(input())
X = ''
Y = ''
for i in range(n):
    xy = input().strip().split()
    if i % 2 == 0:
        X = X[0:] + xy[0] + ' '
        Y = Y[0:] + xy[1] + ' '
    else:
        X = X[0:] + xy[1] + ' '
        Y = Y[0:] + xy[0] + ' '
X = X.strip().split()
Y = Y.strip().split()
for i in range(n):
    X[i] = int(X[i])
    Y[i] = int(Y[i])
X.sort()
Y.sort()
check = input()
if check == 'Zig-Zag':
    print(X[0])
    print(Y[n-1])
else:
    print(Y[0])
    print(X[n-1])