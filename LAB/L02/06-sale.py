totalDays = int(input('How many day : '))
priceSum = 0
promotion = 0.05
for day in range(totalDays):
    price = float(input(f'Input price in day {day+1} : '))
    priceSum += (price - (price * promotion))
    promotion += 0.01

print(f'Summary price = {priceSum:.2f}')    