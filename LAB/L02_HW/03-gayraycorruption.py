H = int(input('hight of electric poles : '))
nPoles = int(input('number of electric poles : '))
poles = []
delta = None
for iteration in range(nPoles):
    poles.append(int(input()))

if max(poles) > ((sorted(poles)[-2])*3):
    gayray = max(poles)
    poles.remove(max(poles))
    C = int(sum(poles)/len(poles)) + int(gayray/int(gayray/max(poles)))
    if H <= 1:
        if C <= 3000:
            corruption = 'NO'
        else:
            delta = 3000 - C
            corruption = 'YES'
    elif H > 1 and H <= 4:
        if C <= 10000:
            corruption = 'NO'
        else:
            delta = 10000 - C
            corruption = 'YES'
    elif H > 4 and H <= 8:
        if C <= 50000:
            corruption = 'NO'
        else:
            delta = 50000 - C
            corruption = 'YES'
    elif H > 8:
        if C <= 100000:
            corruption = 'NO'
        else:
            delta = 100000 - C
            corruption = 'YES'
else:

    C = int(sum(poles)/nPoles)

    if H <= 1:
        if C <= 1000:
            corruption = 'NO'
        else:
            delta = 1000 - C
            corruption = 'YES'
    elif H > 1 and H <= 4:
        if C <= 5000:
            corruption = 'NO'
        else:
            delta = 5000 - C
            corruption = 'YES'
    elif H > 4 and H <= 8:
        if C <= 30000:
            corruption = 'NO'
        else:
            delta = 30000 - C
            corruption = 'YES'
    elif H > 8:
        if C <= 75000:
            corruption = 'NO'
        else:
            delta = 75000 - C
            corruption = 'YES'
if delta != None:
    print(f'Avg : {C}\n{corruption} {abs(delta)}')
else:
    print(f'Avg : {C}\nNO')
