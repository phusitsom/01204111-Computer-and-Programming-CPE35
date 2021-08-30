H = float(input("Hight : "))
C = float(input("Cost : "))
if H < 1:
    if C <= 1000:
        print("NO")
    else:
        print("YES")
elif H >= 1 and H <= 4:
    if C == 1001:
        print('YES')
    elif C <= 5000:
        print("NO")
    else:
        print("YES")
elif H > 4 and H <= 8:
    if C <= 30000:
        print("NO")
    else:
        print("YES")
elif H > 8:
    if C <= 75000:
        print("NO")
    else:
        print("YES")