import math
par = [0,0,0,0,0,0,0,0,0]
stroke = [0,0,0,0,0,0,0,0,0]
new_stroke = 0
for i in range(9):
    par[i], stroke[i], c = [int(e) for e in input().strip().split()]
    if c == 1:
        new_stroke += min(par[i]+2, stroke[i])
all_score = math.floor((new_stroke*1.5-sum(par))*0.8)
print(sum(stroke))
print(all_score)
print(sum(stroke)-all_score)