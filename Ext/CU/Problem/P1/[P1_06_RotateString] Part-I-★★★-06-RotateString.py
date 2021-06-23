Type = input()
n = int(input())
check = True
if Type == '180':
    s = input().strip()
    L = len(s)
    for i in range(n-1):
        new_s = input().strip()
        if L != len(new_s):
            check = False
        s += new_s
    if check:
        for i in range(n):
            print(s[-(i*L)-1:-((i+1)*L)-1:-1])
    else:
        print('Invalid size')
if Type == '90':
    s = input().strip()
    L = len(s)
    for i in range(n - 1):
        new_s = input().strip()
        if L != len(new_s):
            check = False
        s += new_s
    if check:
        for i in range(L):
            print(s[-L+i::-L])
    else:
        print('Invalid size')
if Type == 'flip':
    s = input().strip()
    L = len(s)
    s = s[::-1]
    for i in range(n - 1):
        new_s = input().strip()
        if L != len(new_s):
            check = False
        s += new_s[::-1]
    if check:
        for i in range(L):
            print(s[i*L:(i+1)*L])
    else:
        print('Invalid size')