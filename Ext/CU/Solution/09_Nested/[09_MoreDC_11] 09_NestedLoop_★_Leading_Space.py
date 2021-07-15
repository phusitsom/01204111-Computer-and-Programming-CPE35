n = int(input())
for i in range(n):
    s = input()
    c = 0
    if s != '':
        while s[c] == '.':
            c += 1
        k = c//2
        s = '.'*k + s[c:]
    print(s)
