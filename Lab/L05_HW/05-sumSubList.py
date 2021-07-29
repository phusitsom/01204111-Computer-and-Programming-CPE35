a = list(map(int, input().split()))
while True:
    x, y = map(int, input().split())
    if x < 0: x = len(a)+x
    if y < 0: y = len(a)+y
    if (x >= len(a) or x < 0) and (y >= len(a) or y < 0): print("x and y Bad Input")
    elif y >= len(a) or y <0: print("y Bad Input")
    elif x >= len(a) or x < 0: print("x Bad Input")
    else:
        if x>y: break
        print(sum(a[x:y+1]))