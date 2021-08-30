total = 0

def plus(total,value):
    return total + value

def minus(total,value):
    return total - value

def ops(listOfFood):
    for food in listOfFood:
        value, operator = map(int,food.split())
        global total
        if operator == -1:
            total = minus(total, value)
        else:
            total = plus(total, value)
    return total

def main():
    n = int(input("How many food you have : "))
    listOfFood = [input() for i in range(n)]
    print(ops(listOfFood))

if __name__ == '__main__':
    main()
    