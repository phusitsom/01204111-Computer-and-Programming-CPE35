def add_poly(p1, p2):
    add = {}
    m = p1
    n = p2
    if len(p2) < len(p1):
        m, n = n, m
    for (t, x) in n:
        add[x] = t
    for (t, x) in m:
        if x in add:
            add[x] += t
        else: add[x] = t
    ans = []
    for k in sorted(add,reverse = True):
        if add[k] != 0:
            ans.append((add[k], k))
    return ans

def mult_poly(p1, p2):
    mul = {}
    for (n1,x1) in p1:
        for (n2,x2) in p2:
            if x2 + x1 in mul:
                mul[x1 + x2] += n1 * n2
            else: mul[x1 + x2] = n1 * n2
    ans = []
    for k in sorted(mul,reverse = True):
        if mul[k] != 0:
            ans.append((mul[k], k))
    return ans

for i in range(3):
    exec(input().strip())