import math


class MyMath:

    def __init__(self) -> None:
        self.pi = 3.14159076984979535041

    def is_even(self,  number: int) -> bool:
        return number % 2 == 0

    def fac(self, number: int) -> int:
        return math.factorial(number)

    def is_prime(self,  number: int) -> bool:
        for i in range(3, number):
            if number % i == 0:
                return False
        else:
            return True

    def divide_by(self, number: int, divisor: int) -> bool:
        return number/divisor == number//divisor

    def ten_to_bi(self,  number: int) -> str:
        return bin(number)[2:]

    def ten_to_oct(self,  number: int) -> str:
        return oct(number)[2:]

    def ten_to_sixteen(self,  number: int) -> str:
        return hex(number)[2:].upper()

    def int_to_roman(self,  number: int):

        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = ["M", "CM", "D", "CD", "C", "XC",
               "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_number = ''
        i = 0
        while number > 0:
            for _ in range(number // val[i]):
                roman_number += syb[i]
                number -= val[i]
            i += 1

        return roman_number


my_math = MyMath()
num = int(input("Please Enter Number : "))
k = int(input("Divide by? : "))

if my_math.is_even(num):
    print('This number is even number.')
else:
    print('This number is not even number.')

if num <= 20:
    print(f'factorial is {my_math.fac(num):,.0f}.')
else:
    print('factorial TOO LONG')

if my_math.is_prime(num):
    print('This number is a prime number.')
else:
    print('This number is not a prime number.')

if(my_math.divide_by(num, k)):
    print(f'{num} is divisible by {k}')
else:
    print(f'{num} is not divisible by {k}')

print(f'{num} is {my_math.ten_to_bi(num)} in base 2.')
print(f'{num} is {my_math.ten_to_oct(num)} in base 8.')
print(f'{num} is {my_math.ten_to_sixteen(num)} in base 16.')
print(f'{num} is {my_math.int_to_roman(num)} in roman numeral system.')
print(f'PI is {my_math.pi:.20f}')
