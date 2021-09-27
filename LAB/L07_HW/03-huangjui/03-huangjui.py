land = []
while True:
    inp = [float(y) for y in input().split()]
    if inp == []:
        break
    land.append(inp)
minval = float('inf')
try:
    for i in range(len(land)-1):
        for j in range(len(land[i])-1):
            lsum = land[i+1][j+1]*1.1+land[i][j+1]*1.1
            sum1 = land[i][j]+land[i+1][j]*1.21+lsum
            sum2 = land[i+1][j]+land[i][j]*1.21+lsum
            minval = min(minval, min(sum1, sum2))
    print(f'{minval:.2f}')
except IndexError:
    print("Can't Buy")
