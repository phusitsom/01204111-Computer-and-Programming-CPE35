import numpy as np


def read_data():
    # อา่นขอ้มลูจากแป้นพมิพ์จากนัน้สรา้งและคนือาเรยส์องตัว
    # weight เป็ นอาเรยส์ ามชอ่ งเก็บน้าหนักของคะแนนกลางภาค ปลายภาค และโครงงาน (float) #dataเป็นอาเรยข์นาดn4เก็บขอ้มลูนักเรยีนnคนแตล่ะคนมขีอ้มลู
    # เลขประจาตัว คะแนนกลางภาค ปลายภาค และโครงงาน (int)
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data


def report_lower_than_mean(weight, data):
    # แสดงเลขประจาตัวทไี่ ดค้ ะแนนรวมตา่ กวา่ คะแนนเฉลยี่ #ใหแ้สดงบนบรรทัดเดยีวกันหมดคั่นดว้ยเครอื่งหมายจลุภาคและชอ่งวา่งหนงึ่ชอ่ง
    # เรยี งตามลาดับทปี่ รากฎใน data ถา้ ไมม่ ใี ครไดต้ า่ กวา่ คะแนนเฉลยี่ เลย ใหแ้ สดงคาวา่ None
    code = data[:, 0].reshape(data.shape[0])
    score = data[:, 1:]
    all_score = np.dot(score, weight)
    avg = np.sum(all_score) // len(all_score)
    ans = code[all_score < avg]
    x = [str(i) for i in ans]
    if x != []:
        return print(", ".join(x))
    else:
        return print('None')


exec(input().strip())  # ตอ้ งมคี าสั่งน้ี ตรงนี้ ตอนสง่ ให ้ Grader ตรวจ
