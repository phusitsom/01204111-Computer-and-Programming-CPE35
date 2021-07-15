n = input()
k = []
for i in range(int(n)):
    x, y = [float(e) for e in input().split()]
    m = [(x**2+y**2), i+1, x, y]
    k.append(m)
k.sort()
print('#' + str(k[2][1]) + ':' +
      ' (' + str(k[2][2]) + ', ' + str(k[2][3]) + ')')
