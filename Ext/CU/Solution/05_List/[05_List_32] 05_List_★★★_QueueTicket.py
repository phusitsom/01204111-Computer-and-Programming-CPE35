n = int(input())
ans = []
tic = []
time_t = []
x = -1
avg = 0
m = 0
for i in range(n):
    c = input().split()
    if c[0] == 'reset':
        r = int(c[1])
    if c[0] == 'new':
        ans.append('ticket ' + str(r))
        tic.append(r)
        time_t.append(int(c[1]))
        r += 1
    if c[0] == 'next':
        x += 1
        ans.append('call ' + str(tic[x]))
    if c[0] == 'order':
        ans.append('qtime ' + str(tic[x]) + ' ' + str(int(c[1])-time_t[x]))
        avg += int(c[1])-time_t[x]
        m += 1
    if c[0] == 'avg_qtime':
        ans.append('avg_qtime ' + str(round(avg/m, 4)))
for i in range(len(ans)):
    print(ans[i])
