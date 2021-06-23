s = input()
c = False
for i in range(len(s)):
    if s[i] == '[':
        s = s[:i] + '(' + s[i + 1:]
        c = True
    elif s[i] == ']':
        s = s[:i] + ')' + s[i + 1:]
        c = True
    elif s[i] == '(':
        s = s[:i] + '[' + s[i + 1:]
        c = True
    elif s[i] == ')':
        s = s[:i] + ']' + s[i + 1:]
        c = True
print(s)