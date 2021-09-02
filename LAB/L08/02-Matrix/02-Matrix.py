import numpy
import re
with open(input('File name: ')) as file:
    fr = file.read()
    nparrays = list(map(lambda x: numpy.array(list(map(lambda y: list(
        map(int, y.split())), x.splitlines()))), re.findall(r"[0-9]+[^*+]+", fr)))
    ops = re.findall(r"[*+]", fr)

for i in range(len(nparrays)-1):
    if i == 0:
        temp = nparrays[0]
    if ops[i] == "*":
        temp = numpy.matmul(temp, nparrays[i+1])
    elif ops[i] == "+":
        temp += nparrays[i+1]

for i in range(len(temp)):
    for j in range(len(temp[0])):
        print(f"{temp[i][j]:^5}", end=" ")
    print()
