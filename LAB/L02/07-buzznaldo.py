totalMins = int(input('How long have Buzz played ?: '))  # mins
h, m = divmod(totalMins, 60)
if m > 20:
    h, m = h+1, 0
if h >= 5:
    prom = 0.3
elif h >= 4:
    prom = 0.2
elif h >= 2:
    prom = 0.1
else:
    prom = 0
print(f'Total price is {int(((h*900)) - ((h*900)*prom))} baht.')
