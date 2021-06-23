dna = input().strip().upper()
c = True
for i in range(len(dna)):
    if not dna[i] in 'ATCG':
        c = False
        break
if c:
    oper = input().strip().upper()
    if oper == 'R':
        code = 'ACTG'
        ans = ''
        for i in range(len(dna)):
            ans += code[(code.find(dna[i])+2)%4]
        print(ans[::-1])
    elif oper == 'F':
        count = [0,0,0,0]
        for i in range(len(dna)):
            if dna[i] == 'A':
                count[0] += 1
            elif dna[i] == 'T':
                count[1] += 1
            elif dna[i] == 'G':
                count[2] += 1
            elif dna[i] == 'C':
                count[3] += 1
        print('A='+str(count[0])+',', 'T='+str(count[1])+',', 'G='+str(count[2])+',', 'C='+str(count[3]))
    elif oper == 'D':
        duo = input().strip().upper()
        c = 0
        for i in range(len(dna)-1):
            if dna[i:i+2] == duo:
                c += 1
        print(c)
else:
    print('Invalid DNA')