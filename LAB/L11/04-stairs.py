def stair(n): 
    if n < 0 : return 0
    elif not n : return 1
    return stair(n-1)+stair(n-2)+stair(n-3)
n = int(input(f"n : "))
print(stair(n))