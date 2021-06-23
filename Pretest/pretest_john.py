import numpy as np
w, h = list(map(int, input().split()))
farm_p = []
for i in range(h):
    ele = list(map(int, input().split()))

    farm_p.append(ele)

farm_p_arr = np.array(farm_p)
ind_y, ind_x = np.where(farm_p_arr == 0)
replace_val = []

for i in range(len(ind_y)):
    n = 4
    if (farm_p_arr[ind_y[i]-1] == farm_p_arr[h-1])[0] == True:
        up = 0
        n = n -1
        
    else: 
        up = farm_p_arr[ind_y[i]-1,ind_x[i]]
        if up == 0: n = n -1

    try: 
        down = farm_p_arr[ind_y[i]+1,ind_x[i]]
        if down == 0: n = n -1
    except: 
        down = 0
        n = n -1
        

    try: 
        left = farm_p_arr[ind_y[i],ind_x[i]-1]
        if left == 0: n = n -1
    except: 
        left = 0
        n = n -1
        

    try: 
        right = farm_p_arr[ind_y[i],ind_x[i]+1]
        if right == 0: n = n -1
    except: 
        right = 0
        n = n -1

    if n != 0: replace_val.append(int((up + down + left + right)/n))
    else: replace_val.append(0)

for i in range(len(ind_y)):
    farm_p_arr[ind_y[i],ind_x[i]] = replace_val[i]

min_lst = []
max_lst = []
for j in range(h):
    min_lst.append(min(farm_p_arr[j]))
    max_lst.append(max(farm_p_arr[j]))

min_sum = sum(min_lst)
max_sum = sum(max_lst)

print('Min :', min_sum)
print('Max :', max_sum)