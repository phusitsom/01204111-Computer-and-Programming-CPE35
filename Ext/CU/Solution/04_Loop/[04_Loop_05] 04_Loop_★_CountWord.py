key = input()
s = input()
p = ['"', '(', ')', ',', '.', "'"]
c = 0
for i in range(len(s)):
    if s[i] in p:
        s = s[:i] + ' ' + s[i+1:]
s = s.strip().split()
for i in range(len(s)):
    if s[i] == key:
        c += 1
print(c)
