lst = list([int(input(i+": ")), i] for i in ["A", "B", "C"])
while True:
    lst.sort()
    if lst[1][0] == 0 and lst[2][0] == 0:
        break
    lst[0][0], lst[1][0], lst[2][0] = lst[0][0]+1, lst[1][0]-1, lst[2][0]-1
print(lst[0][1])
