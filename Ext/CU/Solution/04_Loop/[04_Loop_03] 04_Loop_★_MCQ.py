key = input()
ans = input()
count = 0
if len(key) != len(ans):
    print("Incomplete answer")
else:
    for i in range(len(key)):
        if key[i] == ans[i]:
            count += 1
    print(count)