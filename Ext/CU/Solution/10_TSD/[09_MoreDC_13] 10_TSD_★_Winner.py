n = int(input())
winner = []
team = set()
l = set()
for i in range(n):
    s = input().split()
    team.update(s)
    l.add(s[1])
winner = list(team - l)
print(sorted(winner))