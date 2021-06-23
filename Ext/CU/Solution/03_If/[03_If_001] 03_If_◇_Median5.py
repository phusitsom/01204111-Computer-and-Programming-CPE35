a = input()
b = input()
c = input()
d = input()
e = input()
x = 0
y = 0
if(a>b):
    x = a
    a = b
    b = x
if(c>d):
    x = c
    c = d
    d = x
if(a>c):
    x = b
    b = d
    d = x
    c = a
a = e
if(a>b):
    x = a
    a = b
    b = x
if(c>a):
    x = b
    b = d
    d = x
    a = c
if(a>d):
    print(d)
else: print(a)