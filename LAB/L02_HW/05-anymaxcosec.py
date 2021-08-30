count,count_m,old_inp=1,0,''
while True:
 inp=input()
 if inp=='0':break
 count = count+1 if inp==old_inp else 1
 old_inp=inp
 if count>count_m:count_m,mx=count,old_inp
print(f'{count_m}\n{mx}')

# from itertools import groupby
# test_list = [None]
# while test_list[-1] != '0': test_list.append(input()) 
# res = {}
# for key, val in groupby(test_list[1:]):
#     sub = sum(1 for i in val)
#     if res.get(key, float('-inf')) < sub:
#         res.pop(key, None)
#         res[key] = sub
# maxVal = max(res, key=res.get)
# print(f'{res[maxVal]}\n{maxVal}')