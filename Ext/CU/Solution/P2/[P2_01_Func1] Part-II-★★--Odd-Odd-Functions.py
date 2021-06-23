def is_odd(n):
    # คืน (True/False) ว่า n เป็นจ านวนคี่หรือไม่
    if n % 2 == 0:
        return False
    else:
        return True


def has_odds(x):
    # คืน (True/False) ว่า x เป็นลิสต์ที่มีข ้อมูลบางตัวเป็นจ านวนคี่
    for i in x:
        if i % 2 != 0:
            return True
    return False


def all_odds(x):
    # คืน (True/False) ว่า x เป็นลิสต์ที่มีข ้อมูลทุกตัวเป็นจ านวนคี่
    c = 0
    for i in x:
        if i % 2 == 1:
            c += 1
    if len(x) == c:
        return True
    else:
        return False


def no_odds(x):
    # คืน (True/False) ว่า x เป็นลิสต์ที่มีไม่มีข ้อมูลที่เป็นจ านวนคี่เลย
    for i in x:
        if i % 2 != 0:
            return False
    return True


def get_odds(x):
    # คืนลิสต์ที่มีจ านวนคี่ที่มีเก็บในลิสต์ x (ล าดับก่อนหลังให ้เป็นไปตามล าดับเดียวกับใน x)
    # เชน่ x = [1,2,3,5,0] จะได ้ผลคือ [1,3,5]
    y = []
    for i in x:
        if i % 2 == 1:
            y.append(i)
    return y


def zip_odds(a, b):
    # คืนลิสต์ที่สร้างจากการน าจ านวนคี่ใน a และ b มาสลับกันเก็บในลิสต์ผลลัพธ์ (เริ่มจากใน a ก่อน)
    # เชน่ a = [0,8,1,2,4,6,5,7,9,2,3] กับ b = [4,19,11,12,10,17] จะได ้คือ
    # [1,19,5,11,7,17,9,3]
    x = get_odds(a)
    y = get_odds(b)
    z = []
    while x != [] and y != []:
        z.append(x[0])
        z.append(y[0])
        x.pop(0)
        y.pop(0)
    z.extend(x)
    z.extend(y)
    return z


exec(input().strip())  # ตอ้ งมคี าสั่งนี้