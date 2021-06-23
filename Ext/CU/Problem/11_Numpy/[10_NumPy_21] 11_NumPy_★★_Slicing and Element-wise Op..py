import numpy as np
def sum_2_rows( M ):
# คนื ผลทไี่ ดจ้ ากการรวมจานวนในคอลัมน์เดยี วกันของแถวทต่ี ดิ กันทลี ะคแู่ ถว
    return M[0::2,:] + M[1::2,:]
def sum_left_right( M ):
# คนื ผลทไี่ ดจ้ ากการรวมจานวนของครง่ึ ซา้ ยกับครง่ึ ขวาของ M
    n= M.shape[1]//2
    return M[:,0:n] + M[:,n:]
def sum_upper_lower( M ):
# คนื ผลทไี่ ดจ้ ากการรวมจานวนของครงึ่ บนกับครง่ึ ลา่ งของ M
    n= M.shape[1]//2
    return M[0:n,:] + M[n:,:]

def sum_4_quadrants( M ): #คนืผลทไี่ดจ้ากการแบง่Mเป็น4จตภุาคและรวมจานวนทต่ีาแหน่งตรงกันในแตล่ะจตภุาค
    n= M.shape[1]//2
    return M[0:n,0:n] + M[0:n,n:] + M[n:,0:n] + M[n:,n:]

def sum_4_cells( M ):
# คนื ผลทไ่ี ดจ้ ากการรวมจานวนทตี่ ดิ กัน 4 ตัว ตามรูปแบบในตัวอยา่ งขา้ งลา่ งนี้
    return M[0::2,0::2] + M[0::2,1::2] + M[1::2,0::2] + M[1::2,1::2]

def count_leap_years( years ):
#years เป็นอาเรยเ์ก็บปี พ.ศ. #คนืจานวนปีในyearsทเี่ป็นปีอทกิสรุทนิ (ปีที่ก.พ.มี29วัน)
    years = years-543
    x = (years % 400 == 0)
    y = (years % 100 != 0)
    z = (years % 4 == 0)
    k = x | (y & z)
    #print(years[k])
    return len(years[k])
exec(input().strip()) # ตอ้ งมคี าส่ังนี้ ตรงนี้ ตอนสง่ ให ้ Grader ตรวจ