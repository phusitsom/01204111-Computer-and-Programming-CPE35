import numpy as np


def p(X):
    # Xเป็นอาเรยข์นาดn2เก็บจานวนโจทยท์ที่า(คอลมัน์0)กบัเกรดเฉลยี่ (คอลมัน์1)ของนักเรยีนnคน #คนือาเรยข์นาดnชอ่งเก็บความน่าจะเป็นทน่ีักเรยีนแตล่ะคนจะเรยีนผา่นวชิาคานวณจากสตูรขา้งบน #ใชค้วามสามารถของNumPyจะเขยีนไดโ้ดยไมต่อ้งใชว้งวน(อยา่งมาก3บรรทัด)
    # ans = np.ndarray(X.shape[0])
    ans = 1 / (1 + np.exp(-(-3.98 + 0.1 * X[:, 0] + 0.5 * X[:, 1])))
    return ans


exec(input().strip())  # ตอ้ งมคี าสง่ั น้ี ตรงน้ี ตอนสง่ ให้Grader ตรวจder ตรวจ
