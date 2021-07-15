score = {'R': 1, 'Y': 2, 'G': 3, 'W': 4, 'B': 5, 'P': 6, 'K': 7, 'X': 0}
n = input()
score1 = 0
score2 = 0
while True:
    if n[0] == '1':
        for i in n[1:]:
            score1 += score[i]
        if n == '1K':
            break
    else:
        for i in n[1:]:
            score2 += score[i]
        if n == '2K':
            break
    n = input()

print(score1, score2)
if score1 > score2:
    print('Player 1 wins')
elif score2 > score1:
    print('Player 2 wins')
else:
    print('Tie')
