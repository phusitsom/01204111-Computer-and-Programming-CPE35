score = input().split()
score.sort()
avg = (float(score[1])+float(score[2]))/2
print(round(avg, 2))
