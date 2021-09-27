n = int(input())
w = '*'


def draw(n):
    for i in range(n-1):
        print(' '*i+w+(' '*n)+(' '*(-((i-n)+2)*2))+w)
    print(" "*(n-1)+w*n)
    for i in range(n-2):
        print(" "*(n-1)+w+(" " * len((w*n)[1:-1]))+w)
    print(" "*(n-1)+w*n)
    for i in range(n-1):
        print(' '*(-((i-n)+2))+w+(' '*n)+(' '*(i*2))+w)


draw(n)
