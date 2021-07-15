s = input().strip().split()
station = {}
while len(s) == 2:
    if s[0] in station:
        if s[1] not in station[s[0]]:
            station[s[0]].append(s[1])
    else:
        station[s[0]] = [s[1]]
    if s[1] in station:
        if s[0] not in station[s[1]]:
            station[s[1]].append(s[0])
    else:
        station[s[1]] = [s[0]]
    s = input().strip().split()
ans = []
if s[0] in station:
    # ans = station[s[0]] ans connect to station[s[0]]
    ans = [i for i in station[s[0]]]
    for i in station[s[0]]:
        for j in station[i]:
            if j not in ans and j != s[0]:
                ans.append(j)
ans.append(s[0])
for i in sorted(ans):
    print(i)
'''s = input().strip().split()
station = {}
while len(s) == 2:
    if s[0] in station:
        if s[1] not in station[s[0]]:
            station[s[0]].append(s[1])
    else:
        station[s[0]] = [s[1]]
    if s[1] in station:
        if s[0] not in station[s[1]]:
            station[s[1]].append(s[0])
    else:
        station[s[1]] = [s[0]]
    s = input().strip().split()
ans = []
if s[0] in station:
    ans = station[s[0]]
    for i in range(len(station[s[0]])):
        for j in station[station[s[0]][i]]:
            if j not in ans and j != s[0]:
                ans.append(j)
ans.append(s[0])
for i in sorted(ans):
    print(i)'''
