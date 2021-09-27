H = float(input("Hight : "))
C = float(input("Cost : "))

thresholds = ((8,75000),
              (4,30000),
              (1,5000),
              (0,1000))

for h, c in thresholds:
    if H > h:
        if C > c:
            print("YES")
        else: 
            print("NO")
        break
