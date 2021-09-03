count, count_m, old_inp = 1, 0, ''
while True:
    inp = input()
    if inp == '0':
        break
    count = count+1 if inp == old_inp else 1
    old_inp = inp
    if count > count_m:
        count_m, mx = count, old_inp
print(f'{count_m}\n{mx}')
