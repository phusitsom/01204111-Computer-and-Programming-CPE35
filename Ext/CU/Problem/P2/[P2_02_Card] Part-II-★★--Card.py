num = {'A':1, 'T':10, 'J':11, 'Q':12, 'K':13}
for i in range(2,10):
    num[str(i)] = i
suit = {'C':1, 'D':2, 'H':3, 'S':4}
n = input().strip()
s = ''
for i in range(0,len(n)-2,2):
    if n[i] != n[i+2]:
        if num[n[i]]-num[n[i+2]] > 0:
             s += '+' + str(num[n[i]]-num[n[i+2]])
        else: s += str(num[n[i]]-num[n[i+2]])
    else:
        if n[i+1] != n[i+3]:
            if suit[n[i+1]]-suit[n[i+3]] > 0:
                s += '+' + str(suit[n[i+1]]-suit[n[i+3]])
            else: s += str(suit[n[i+1]]-suit[n[i+3]])
        else:
            s += '0'
print(s)