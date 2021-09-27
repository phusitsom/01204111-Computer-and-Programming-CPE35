def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y): return (x*y)//gcd(x, y)


a, b = (int(input(f"{i} : ")) for i in ['a', 'b'])
print(f"GCD : {gcd(a,b)}\nLCM : {lcm(a,b)}")
