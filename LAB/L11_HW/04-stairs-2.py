def stair(n): 
    if n < 0 : return 0
    elif not n : return 1
    return stair(n-a)+stair(n-b)+stair(n-c)
n, a, b, c = (int(input(f"{e} : ")) for e in ('n','a','b','c'))
print(stair(n))