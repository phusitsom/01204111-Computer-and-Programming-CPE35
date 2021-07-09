from itertools import groupby
test_list = [None]
while test_list[-1] != '0': test_list.append(input()) 
res = {}
for key, val in groupby(test_list[1:]):
    sub = sum(1 for i in val)
    if res.get(key, float('-inf')) < sub:
        res.pop(key, None)
        res[key] = sub
maxVal = max(res, key=res.get)
print(f'{res[maxVal]}\n{maxVal}')