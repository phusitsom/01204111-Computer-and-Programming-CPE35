
from math import factorial
a, outputList = [], []
for i in range(int(input())):
    for j in range(i+1):
        a.append(str(factorial(i)//(factorial(j)*factorial(i-j))))
    outputList.append(a)
    a = []
print('\n'.join(map(' '.join, list(reversed(outputList)))))
