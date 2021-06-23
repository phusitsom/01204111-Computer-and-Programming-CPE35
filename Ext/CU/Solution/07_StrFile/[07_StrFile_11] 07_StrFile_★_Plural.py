s = input()
if s[-1] == 's' or s[-1] == 'x' or s[-2:] == 'ch':
    s += 'es'
elif s[-1] == 'y' and s[-2] not in ['a','e','i','o','u']:
    s = s[0:-1] +'ies'
else:
    s += 's'
print(s)