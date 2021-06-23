a,b,c,d = [int(i) for i in input().split()]
x=0
if(a>b):
    x=a
    a=b
    b=x
    if(d>=a):
        if(c>d):
            c=c-a
    else: c=c+a
    b=a+c+d
else:
    if(c>a and a>=b):
        d=d+a
    if(d>c):
        b=b+2
    else: b=b*2
print(a,b,c,d)