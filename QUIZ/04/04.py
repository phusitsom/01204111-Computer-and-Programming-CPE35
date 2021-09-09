def read_csv(fn: str):
    with open(fn) as file:
        _items = list(map(lambda x: x.split(','),file.read().splitlines()))
        _keys = [item.pop(0) for item in _items[1:]]
        _val_key = _items.pop(0)[1:]
        
        return {_key:dict(zip(_val_key,tuple(map(int,_item)))) for _key,_item in zip(_keys,_items)}
    
    
fn = input('filename: ')
with open(fn) as file:
    _items = list(map(lambda x: x.split(','),file.read().splitlines()))
    _keys = _items.pop(0)
    
    data = [dict(zip(_keys,_item)) for _item in _items]
    
    
    
con_cov1 = read_csv(fn)

_1 = sum([int(i['Total Cases']) for i in data])
_2 = max(con_cov1.items(), key= lambda x: x[1]['Deaths'])[0]
_3 = max(con_cov1.items(), key= lambda x: x[1]['Deaths']/x[1]['Total Cases'])[0]
_4 = max(con_cov1.items(), key= lambda x: x[1]['Discharged']/x[1]['Total Cases'])[0]

a = t = 0

for v in con_cov1.values():
    a, t = a+v['Active'], t+ v['Total Cases']
    
_5 = f'{a*100/t:.2f}%'

avg_7_days = {}

for item in tuple(con_cov1.items()):
    
    state = item[0]
    day_1_7 = tuple(item[1].values())[4:]
    
    if state not in avg_7_days:
        avg_7_days.setdefault(state,0)
        
    avg_7_days[state] = sum(day_1_7)/7


pri_str_6 = []
for state, avg in sorted(avg_7_days.items(), key= lambda x: x[1], reverse= True)[:5]:
    pri_str_6.append(f"{state} {avg:.0f}")
    
_6 = '\n'.join(pri_str_6)

red_states = []

for item in tuple(con_cov1.items()):
    
    state = item[0]
    day_1_7 = tuple(item[1].values())[4:]
    
    tf = tuple(map(lambda x: x>100,day_1_7))
    
    
    for i in range(len(tf)-4):
        if all(tf[i:i+5]):
            red_states.append(state)
            break
    
_7 = sorted(red_states)

ty = int(input('type: '))
if ty == 7:
    for i in _7:
        print(i)
else:
    print([_1,_2,_3,_4,_5,_6,_7][ty-1])