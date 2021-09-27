distance = int(input('Input distance(kilometer): '))
time = (distance + ((distance % 6) * int(distance/6))) * 10
print(f'It takes {(int(time/60))} hours and {time - (int(time/60)*60)} minutes to reach the destination.')
