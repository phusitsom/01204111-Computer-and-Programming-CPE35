import numpy as np


# คนือาเรยท์มี่ีshapeเป็น(nrow,ncols)ภายในเก็บตารางสตูรคณู (ดตูัวอย่างขา้งลา่ง)
def mult_table(nrows, ncols):
    a = np.arange(nrows).reshape(nrows, 1) + 1
    b = np.arange(ncols).reshape(1, ncols) + 1
    return a*b


exec(input().strip())  # ตอ้ งมคี าสง่ั นี้ ตรงนี้ ตอนสง่ ให้Grader ตรวจ
