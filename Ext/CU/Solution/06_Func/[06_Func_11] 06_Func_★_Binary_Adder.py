a, b = [int(e, 2) for e in input().strip().split()]
c = a+b
print(bin(c)[2:])
