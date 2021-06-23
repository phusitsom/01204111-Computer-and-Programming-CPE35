def factor(N): # N เป็ นจ ำนวนเต็มบวกมำกกว่ำ 1
    k = 2
    ans = []
    while k <= N:
        c = 0
        while N % k == 0:
            N = N//k
            c += 1
        if c != 0:
            ans.append([k,c])
        k += 1
    return ans

exec(input().strip()) # ตอ้ งมคี ำสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ