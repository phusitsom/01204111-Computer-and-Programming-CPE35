n=int(input("N : "))
ar = [int(x) for x in input().split()]
print("no") if (1 in ar[::2] and 2 in ar[::2]) or (1 in ar[1::2] and 2 in ar[1::2]) else print("yes")