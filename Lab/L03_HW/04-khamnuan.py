n = int(input(('Number : ')))
def even_check(num):
    if num % 2 == 0: print('The number is even')
    else: print('The number is odd')
    
def prime_check(num):
    isnotprime = None
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                isnotprime = True
                break
    if isnotprime: print('The number is not prime')
    else: print('The number is prime')

even_check(n)
prime_check(n)

