score = []
#mn = 100
#mx = 0
#n= 0
#summ= 0
File, year = input().strip().split()
infile = open(File, 'r')
for line in infile:
    code, point = line.strip().split()
    point = float(point)
    if year[-2:] == code[0:2] :
        score.append(point)
        #n+=1
        #summ += point
        #mn = min(mn,point)
        #mx = max(mx,point)
infile.close()
score.sort()
if score == []:
    print('No data')
else:
    print(score[0], score[-1], sum(score)/len(score))
    #print(mn,mx,summ/n)