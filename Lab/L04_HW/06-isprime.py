def is_prime(n):
    if n <= 1:
        return False
    for k in range(2, int(n**0.5)+1):
        if n % k == 0:
            return False
    return True
primenums = []
while True:
    n = int(input())
    if n == 0:break
    primenums.append(n) if is_prime(n) else None
for i in range(-(-len(primenums)//10)):
    print(*primenums[:10])
    del primenums[:10]