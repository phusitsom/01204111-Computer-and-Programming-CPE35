result = input()
n = int(input())
score = [0,0,0,0,0,0,0,0,'X',0]
result_new = ''
c = 0
j = 0
for i in range(len(result)):
    if result[i] == '/':
        result_new = result_new[:i] + str(10-int(result[i-1]))
    else:
        result_new = result_new[:i+1] + result[i]
while score[8] == 'X':
    score[j] = 0
    if result[c] == 'X':
        score[j] += 10
        if result[c+1]  == 'X':
            score[j] += 10
        else: score[j] += int(result_new[c+1])
        if result[c+2]  == 'X':
            score[j] += 10
        else: score[j] += int(result_new[c+2])
        #print(score[j],'X')
        c += 1
        j += 1
    else:
        if result[c+1] == '/' :
            score[j] += 10
            if result[c + 2] == 'X':
                score[j] += 10
            else:
                score[j] += int(result_new[c + 2])
            #print(score[j],'/')
            c += 2
            j += 1
        else:
            score[j] += int(result_new[c]) + int(result_new[c + 1])
            #print(score[j],'-')
            c += 2
            j += 1
t = len(result_new)-c
for i in range(t):
    if result[-2] == '/':
        score[9] = 10
    if result_new[-t+i] == 'X':
        score[9] += 10
    else:
        score[9] += int(result_new[-t+i])
#print(score,c)
if n in [1,2,3,4,5,6,7,8,9,10]:
    print(score[n-1])
else:
    print(sum(score))