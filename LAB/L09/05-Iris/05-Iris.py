import json

with open(input('Filename : ')) as file: data = json.loads(file.read())

typ = input('type : ')
avg_sp = {}

for item in data:
    species = item.pop('species')
    val = item.pop(typ)
    if species not in avg_sp:
        avg_sp.setdefault(species,[])
    avg_sp[species].append(val)
    
for species, avg in ((_sp,sum(_v)/len(_v)) for _sp, _v in  avg_sp.items()):
    print(f"{species} = {avg:.2f}")