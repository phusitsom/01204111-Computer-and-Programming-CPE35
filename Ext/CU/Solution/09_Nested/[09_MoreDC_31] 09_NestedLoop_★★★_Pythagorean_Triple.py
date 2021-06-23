def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a

def is_coprime(a, b, c):
    return gcd(gcd(a,b),c) == 1

def primitive_Pythagorean_triples(max_len):
    triple = []
    for c in range(2,max_len+1):
        for b in range(2,c):
            for a in range(2,b+1):
                if a**2 + b**2 == c**2:
                    if is_coprime(a,b,c):
                        triple.append([c,a,b])
                    break
    triple.sort()
    for i in range(len(triple)):
         triple[i] = [triple[i][1],triple[i][2],triple[i][0]]
    return triple

exec(input().strip())  # ตอ้ งมคี าสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ