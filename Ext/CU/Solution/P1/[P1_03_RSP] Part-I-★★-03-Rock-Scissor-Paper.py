n = int(input())
c = 0
score1 = 0
score2 = 0
w2 = ['S R', 'R P', 'P S']
w1 = ['R S', 'P R', 'S P']
while(score1 != n and score2 != n and c!=3*n):
        x = input()
        if x in w1:
            score1 += 1
        elif x in w2:
            score2 += 1
        c += 1
if score1 == n:
    print(score1,score2)
    print('Player 1 wins')
elif score2 == n:
    print(score1, score2)
    print('Player 2 wins')
else:
    print(score1, score2)
    print('Tie')