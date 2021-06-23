def first_fit(L, e): # น ำ e ใสรำยกำรย่อยใ ่ น L ด ้วยวิธี first fit
    for i in range(len(L)):
        if e + sum(L[i]) <= 100:
            L[i].append(e)
            return L
    L.append([e])
    return L

def best_fit(L, e): # น ำ e ใสรำยกำรย่อยใ ่ น L ด ้วยวิธี best fit
    c = 0
    p = -1
    for i in range(len(L)):
        if e + sum(L[i]) <= 100 and c < (e + sum(L[i])):
            p = i
            c = e + sum(L[i])
    if p == -1:
        L.append([e])
    else: L[p].append(e)
    return L

def partition_FF(D): # คืนลิสต์ของลิสต์ที่ได ้จำกกำรแบ่งข ้อมูลใน D ด ้วย first fit
    x = []
    for i in D:
        if x == []:
            x.append([i])
        else:
            first_fit(x,i)
    return x

def partition_BF(D): # คืนลิสต์ของลิสต์ที่ได ้จำกกำรแบ่งข ้อมูลใน D ด ้วย best fit
    x = []
    for i in D:
        if x == []:
            x.append([i])
        else:
            best_fit(x,i)
    return x

exec(input().strip()) # ตอ้ งมคี ำสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ