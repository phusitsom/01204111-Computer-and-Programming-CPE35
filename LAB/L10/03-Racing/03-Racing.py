import json

data = json.load(open(input('Enter json filename : ')))['racer']

distance = int(input('Enter distance (meter) : '))

for racer in data:
    all_x, all_v = racer['_range'], racer['velocity']

    t = 0
    for i, (x, v) in enumerate(zip(all_x, all_v)):
        try:
            if all_x[i+1] <= distance:
                t += (all_x[i+1] - x)/v
            else:
                raise IndexError
        except IndexError:
            t += (distance-x)/v
            break

    racer.update({'time': f'{t:.2f}'})

for result in sorted(data, key=lambda racer: (float(racer['time']),
                                              -racer['response'],
                                              racer['name'])):
    print(result['name'], result['time'])
