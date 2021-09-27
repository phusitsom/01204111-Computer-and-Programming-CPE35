nPoles = int(input('number of electric poles : '))
poles = []
for iteration in range(nPoles):
    poles.append(int(input()))

if max(poles) > ((sorted(poles)[-2])*3):
    print(f'YES\n{max(poles)}')
else:
    print('NO')
