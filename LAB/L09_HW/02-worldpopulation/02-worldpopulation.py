import json

with open(input("File Name: ")) as file:
    data = json.loads(file.read())
    
menu = int(input('Input : '))

print([
    None,
    len(data),
    sum([int(country['population']) for country in data]),
    '\n'.join(map(str,(sum(map(lambda x: x['country'][0].lower() == 'c', data)),sum(map(lambda x: len(x['country'])>5, data))))),
    '\n'.join(map(str,(sum(map(lambda x: 500e6 < int(x['population']), data)) ,sum(map(lambda x: 250e6 < int(x['population']) <= 750e6, data)) ,sum(map(lambda x: int(x['population']) < 10e6, data))))),
    '\n'.join(map(lambda x: f'{x*100:.2f}',(sum([float(coun['World']) for coun in data[:20]]), sum([float(coun['World']) for coun in data[49:150]]))))
][menu])