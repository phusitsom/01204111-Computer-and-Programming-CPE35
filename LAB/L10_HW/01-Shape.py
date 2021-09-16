PI = 3.14


class Rectangle(object):

    def __init__(self, __length: int, __width: int):
        self.length = __length
        self.width = __width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return self.length*2 + self.width*2

    def is_square(self):
        return "This rectangle is square too." if self.length == self.width else "This rectangle is not square."


class Triangle(object):

    def __init__(self, *args):
        self.lenghts = args
        self.perimeter = sum(self.lenghts)

    def area(self):
        _s = self.__perimeter__/2

        return (_s*(_s-self.lenghts[0])*(_s-self.lenghts[1])*(_s-self.lenghts[2]))**0.5

    def perimeter(self):
        return self.__perimeter__

    def is_right_triangle(self):
        x, y, z = sorted(self.lenghts)
        return "This triangle is right triangle too." if x**2+y**2 == z**2 else "This triangle is not right triangle."


class Circle(object):

    def __init__(self, radius: int):
        self.radius = radius

    def area(self):
        return f'{PI*(self.radius**2):.2f}'

    def perimeter(self):
        return f'{2*PI*self.radius:.2f}'


l = int(input("Enter rectangle length : "))
w = int(input("Enter rectangle width : "))
p1 = Rectangle(l, w)
print(f'Area is {p1.area()}.')
print(f'Perimeter is {p1.perimeter()}.')
print(p1.is_square())

l1 = int(input("Enter triangle first side length : "))
l2 = int(input("Enter triangle second side length : "))
l3 = int(input("Enter triangle third side length : "))
p2 = Triangle(l1, l2, l3)
print(f'Area is {p2.area()}.')
print(f'Perimeter is {p2.perimeter()}.')
print(p2.is_right_triangle())

r = int(input("Enter circle radius : "))
p3 = Circle(r)
print(f'Area is {p3.area()}.')
print(f'Perimeter is {p3.perimeter()}.')
