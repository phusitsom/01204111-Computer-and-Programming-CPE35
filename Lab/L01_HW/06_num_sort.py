a,b,c,d = map(int,input().split())
one,two,three,four = 0,0,0,0
if a > b: a, b = b, a
if c > d: c, d = d, c
if a > c: a, c = c, a
if b > d: b, d = d, b
if b > c: b, c = c, b
one, two, three, four = a, b, c, d
print(f'{one} {two} {three} {four}')