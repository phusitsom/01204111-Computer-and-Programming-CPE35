def make_int_list(x):
    # รับสตริง x มำแยกและแปลงเป็น int เก็บใน list แล้วคืนเป็นผลลัพธ์
    # เช่น x = '12 34 5' ได้ผลเป็น [12 34 5]
    x = x.split()
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


def is_odd(e):
    # คืนค่ำจริงเมื่อ e เป็นจ ำนวนคี่ ถ้ำไม่ใช่ คืนค่ำเท็จ
    if e % 2 == 0:
        return False
    else:
        return True


def odd_list(alist):
    # คืน list ที่มีค่ำเหมือน alist แต่มีเฉพำะตัวที่เป็นจ ำนวนคี่
    # เช่น alis = [10, 11, 13, 24, 25] จะได้ [11, 13, 25]
    s = []
    for i in range(len(alist)):
        if is_odd(alist[i]):
            s.append(alist[i])
    return s


def sum_square(alist):
    # คืนผลรวมของก ำลังสองของแต่ละค่ำใน alist
    # เช่น alist = [1,3,4] ได้ผลเป็น (1*1 + 3*3 + 4*4) = 26
    s = 0
    for i in range(len(alist)):
        s += alist[i] ** 2
    return s


exec(input().strip())  # ต้องมีบรรทัดนี้เมื่อส่งไป grader
