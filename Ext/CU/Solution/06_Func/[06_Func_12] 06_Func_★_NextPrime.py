def is_prime(n):
    # ทดสอบว่า n เป็นจ านวนเฉพาะหรือไม่
    if n <= 1:
        return False
    for k in range(2, int(n**0.5)+1):
        if n % k == 0:
            return False
    return True


def next_prime(N):
    # คืนจ านวนเฉพาะตัวที่มีค่าน้อยสุดที่มากกว่า N
    x = int(N)+1
    while not is_prime(x):
        x += 1
    return x


def next_twin_prime(N):
    # คืนจ านวนเฉพาะสองค่าที่เป็น twin prime ที่มีค่าน้อยสุดที่มากกว่า N
    x = int(N) + 1
    n = next_prime(x)
    m = next_prime(n)
    while not m - n == 2:
        n = m
        m = next_prime(n)
    return '(' + str(n) + ', ' + str(m) + ')'


exec(input().strip())  # ตอ้ งมคี าสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ
