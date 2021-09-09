import json

with open(input('Filename : ')) as file:
    data = json.loads(file.read())

inp = input('Data : ')

found = tuple(map(lambda x: inp in x.values(), data))

if any(found):
    
    print('Found in blacklist')
    
    for k,v in data[found.index(1)].items(): 
        print(f'{k} : {v}')
    
else: print('Not found in blacklist')