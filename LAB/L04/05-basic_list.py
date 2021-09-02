from statistics import median
inplst = []
while len(inplst) < 5:
    inp = int(input("Enter a positive number: "))
    if inp <= 0:
        pass
    else:
        inplst.append(inp)
print(f"sum: {sum(inplst)}\nmin: {min(inplst)}\nmax: {max(inplst)}\nmed: {median(inplst)}")
