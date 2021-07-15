s = input() + ' '
n = s[0]
count = 0
word = ''
for i in range(len(s)):
    if n == s[i]:
        count = count+1
    else:
        word = word[0:] + str(n) + ' ' + str(count) + ' '
        n = s[i]
        count = 1
print(word)
