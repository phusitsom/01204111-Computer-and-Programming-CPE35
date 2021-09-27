from math import sin, cos, tan, radians
degree = radians(int(input('Degree : ')))
print("sin : {}\ncos : {}\ntan : {}".format(*[map(lambda x: round(x, 2),
                                                  [sin(degree),
                                                   cos(degree),
                                                   tan(degree)])]))
