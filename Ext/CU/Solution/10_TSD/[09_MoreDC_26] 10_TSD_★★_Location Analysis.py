n = int(input())
user = {}
user_name = []
for i in range(n):
    s = input().strip().split(': ')
    t = s[1].split(', ')
    user[s[0]] = set(t)
    user_name.append(s[0])
name = input()
user_name.remove(name)
ans = []
for name1 in user_name:
    if user[name] & user[name1] != set():
        ans.append(name1)
if ans == []:
    print('Not Found')
else:
    for i in ans:
        print(i)
